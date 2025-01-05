import os
from dektools.file import sure_dir, write_file
from dektools.design.node.base import NodeBase, NodeTypes, MixinTrans
from dektools.func import FuncAnyArgs
from deknetreq.design.apply import NodeManagerNet
from ....utils.common import optimize_svg
from ...res import SvgYamlRes


class NodeSvg(NodeBase):
    need_g_wrapper = False


class NodeCanvas(NodeSvg):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = self.manager.default_width
        self.height = self.manager.default_height

    def set_wh(self, w, h):
        self.width = w
        self.height = h

    def pv(self, value, ratio=1):
        if isinstance(value, float):
            return self.width * value * ratio
        return value


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

    def make(self, args, params, attrs):
        return self.manager.render_by_struct(self.draw(self.new_proxy(attrs)), params)

    def draw(self, proxy):
        raise NotImplementedError


node_types = NodeTypes()


class SvgManager(NodeManagerNet, MixinTrans):
    types = node_types

    res_cls_setup = SvgYamlRes

    default_width = 1024
    default_height = default_width

    async def dump(self, path):
        sure_dir(path)
        async for item_name, name, params in self.fetch_items():
            item = self.make_svg(item_name, params=params)
            write_file(os.path.join(path, name + '.svg'), b=item)

    def entries(self, args=None, params=None, attrs=None):
        for name in self.entry_names:
            yield name, self.make_svg(name, args, params, attrs)

    def make_svg(self, name, args=None, params=None, attrs=None):
        node = self.get_node(name)
        content = node.make(args or [], params or {}, attrs or {})
        return optimize_svg(
            f'<svg viewBox="0 0 {node.width} {node.height}" '
            f'xmlns="http://www.w3.org/2000/svg" '
            f'xmlns:xlink="http://www.w3.org/1999/xlink">{content}</svg>'
        ).encode('utf-8')

    def render_by_struct(self, data, params):
        if isinstance(data, str):
            return data
        result = ""
        for label, attrs in data.items():
            tag, trans = self.parse_call_label(params, label)
            attrs = attrs.copy()
            children = attrs.pop('+', None)
            sa = "".join(f' {k}="{v}"' for k, v in attrs.items() if v not in ('', None))
            if children is None:
                result += f"<{tag}{trans}{sa}/>"
            else:
                result += f"<{tag}{trans}{sa}>{self.render_by_struct(children, params)}</{tag}>"
        return result

    def parse_call_label(self, params, label, node=None):
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

        label = self.trans_var(label, params)

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
