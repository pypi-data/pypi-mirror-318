import os
import re
from dektools.func import FuncAnyArgs
from dektools.yaml import yaml
from dektools.file import read_text, FileHitChecker, sure_dir, write_file
from ...utils.common import optimize_svg
from .....font.const import font_extensions


class Node:
    need_g_wrapper = False

    def __init__(self, manager):
        self.manager = manager

    def render(self, params, attrs):
        raise NotImplementedError()


class NodeCanvas(Node):
    def __init__(self, manager, width, height):
        super().__init__(manager)
        self.width = width
        self.height = height

    def pv(self, value, ratio=1):
        if isinstance(value, float):
            return self.width * value * ratio
        return value


class FunctionNode(NodeCanvas):
    re_var = r'\$\$([^\W0-9]\w*)[\^]?'

    def __init__(self, manager, name, args, params, body):
        super().__init__(manager, *args)
        self.name = name
        self.body = body
        self.params = params

    @classmethod
    def trans_var(cls, s, params):
        return yaml.loads(re.sub(cls.re_var, lambda x: str(params[x.group(1)]), s))

    @classmethod
    def _translate_data(cls, params, data):
        result = {}
        for k, v in data.items():
            if isinstance(v, str):
                v = cls.trans_var(v, params)
            if v is not None:
                result[k] = v
        return result

    def render(self, params, attrs):
        params = {**self.params, **params}
        result = ""
        for key, value in self.body.items():
            value = value or {}
            name, trans = self.manager.parse_call_label(params, key, self)
            node = self.manager.get_node(name, self.width, self.height)
            content = node.render(params, self._translate_data(params, value))
            result += f"""<g{trans}>{content}</g>""" if trans or node.need_g_wrapper else content
        return result


class SvgNode(Node):
    need_g_wrapper = True

    def __init__(self, manager, content):
        super().__init__(manager)
        self.content = content

    def render(self, params, attrs):
        if attrs:
            return self.manager.render_by_struct({'g': {**attrs, '+': self.content}}, params)
        return self.content


class TagNode(Node):
    def __init__(self, manager, name):
        super().__init__(manager)
        self.name = name

    def render(self, params, attrs):
        return self.manager.render_by_struct({self.name: attrs}, params)


class NodeElement(NodeCanvas):
    name = None
    spec = {}

    class Proxy:
        def __init__(self):
            self.params = {}

        def __getattr__(self, item):
            return self.params[item]

        def __setitem__(self, key, value):
            self.params[key] = value

    def new_proxy(self, attrs):
        proxy = self.Proxy()
        attrs = {**self.spec, **attrs}
        for k, v in attrs.items():
            if callable(v):
                v = FuncAnyArgs(v)(self.width, self.height, proxy)
            proxy[k] = v
        return proxy

    def render(self, params, attrs):
        return self.manager.render_by_struct(self.draw(self.new_proxy(attrs)), params)

    def draw(self, proxy):
        raise NotImplementedError()


class Manager:
    ignore_file = '.svgdesignignore'
    entry_marker = '>>'
    default_width = 1024
    default_height = default_width
    function_node_cls = FunctionNode
    svg_node_cls = SvgNode
    tag_node_cls = TagNode

    element_map = {}

    @classmethod
    def parse_args(cls, args):
        if not args:
            return cls.default_width, cls.default_height
        rr = re.match(r"^[0-9. ]+", args)
        if rr:
            wh = rr.group()
        else:
            wh = ""
        items = [x.strip() for x in wh.strip().split()]
        items = items + (2 - len(items)) * [""]
        items = [int([cls.default_width, cls.default_height][i] if x == "" else x) for i, x in enumerate(items)]
        return items[0], items[1]

    @classmethod
    def parse_call_label(cls, params, label, node=None):
        def pv(tf, value):
            if node and tf in {'translate'}:
                return node.pv(value)
            return value

        def transform(s):
            for k, v in transform_map.items():
                if s.startswith(k):
                    tf = [str(pv(v, float(x) if '.' in x else int(x))) for x in s[len(k):].split(',')]
                    return f"{v}({','.join(tf)})"
            return ""

        transform_map = {'t': 'translate', 's': 'scale', 'sk': 'skew', 'r': 'rotate'}

        label = cls.function_node_cls.trans_var(label, params)

        kl = label.split(" ", 1)
        name = kl[0]
        if len(kl) == 2:
            items = [transform(x) for x in kl[1].split() if x and not x.startswith('-')]
        else:
            items = []
        if items:
            trans = f' transform="{" ".join(items)}"'
        else:
            trans = ""
        return name, trans

    def __init__(self):
        self.entry_names = []
        self.function_map = {}
        self.svg_map = {}
        self.font_map = {}

    def dump(self, path, params=None, attrs=None):
        sure_dir(path)
        for name, content in self.entries(params, attrs):
            write_file(os.path.join(path, name + '.svg'), s=content)

    def entries(self, params=None, attrs=None):
        for name in self.entry_names:
            yield name, self.make_svg(name, params, attrs)

    def make_svg(self, name, params=None, attrs=None):
        node = self.get_node(name)
        content = node.render(params or {}, attrs or {})
        return optimize_svg(
            f'<svg viewBox="0 0 {node.width} {node.height}" '
            f'xmlns="http://www.w3.org/2000/svg" '
            f'xmlns:xlink="http://www.w3.org/1999/xlink">{content}</svg>'
        )

    def get_node(self, name, width=None, height=None):
        return self.function_map.get(name) or \
            self.new_svg_node(name) or \
            self.element_map.get(name) and self.element_map[name](
                self,
                self.default_width if width is None else width,
                self.default_height if height is None else height,
            ) or \
            self.tag_node_cls(self, name)

    def new_svg_node(self, name):
        path = self.svg_map.get(name)
        if path:
            return self.svg_node_cls(self, read_text(path))

    @classmethod
    def render_by_struct(cls, data, params):
        if isinstance(data, str):
            return data
        result = ""
        for label, attrs in data.items():
            tag, trans = cls.parse_call_label(params, label)
            attrs = attrs.copy()
            children = attrs.pop('+', None)
            sa = "".join(f' {k}="{v}"' for k, v in attrs.items() if v not in ('', None))
            if children is None:
                result += f"<{tag}{trans}{sa}/>"
            else:
                result += f"<{tag}{trans}{sa}>{cls.render_by_struct(children, params)}</{tag}>"
        return result

    def load_data(self, data_map):
        for label, body in data_map.items():
            body = body.copy()
            params = body.pop('$$', None) or {}
            array = label.split(" ", 1)
            name = array[0]
            if len(array) == 2:
                args = array[1]
            else:
                args = None
            args = self.parse_args(args)
            if name.endswith(self.entry_marker):
                name = name[:len(name) - len(self.entry_marker)]
                self.entry_names.append(name)
            self.function_map[name] = self.function_node_cls(self, name, args, params, body)

    def load_file_yaml(self, path):
        self.load_data(yaml.load(path))

    def load_file_svg(self, path):
        name = os.path.splitext(os.path.basename(path))[0]
        self.svg_map[name] = path

    def load_file_font(self, path):
        name = os.path.splitext(os.path.basename(path))[0]
        self.font_map[name] = path

    def load_path(self, *paths):
        def walk(fp, match, _):
            if match:
                return
            ext = os.path.splitext(fp)[-1].lower()
            if ext == '.svg':
                self.load_file_svg(fp)
            elif ext == '.yaml':
                self.load_file_yaml(fp)
            elif ext in font_extensions:
                self.load_file_font(fp)

        for path in paths:
            FileHitChecker(path, self.ignore_file).walk(walk)

    @classmethod
    def element(cls, element_cls):
        if element_cls.name:
            name = element_cls.name
        else:
            name = element_cls.__name__
        cls.element_map[name] = element_cls
        return element_cls
