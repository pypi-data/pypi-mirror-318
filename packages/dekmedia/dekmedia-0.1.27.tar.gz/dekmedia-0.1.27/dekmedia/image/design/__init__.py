import os
import re
from collections import OrderedDict
from PIL import Image
from skimage.io._plugins.pil_plugin import pil_to_ndarray, ndarray_to_pil
from dektools.yaml import yaml
from dektools.file import read_file, FileHitChecker, sure_dir
from dektools.module import get_module_attr
from deknetreq.design import NetReqDesign
from dektools.dict import dict_merge
from ...font.const import font_extensions
from ..const import image_extensions
from ..psd import PsdCanvas
from ..svg.load import load_svg
from ..svg.design import Manager as SvgManager


class Node:
    def __init__(self, manager: 'Manager', content):
        self.manager = manager
        self.content = content

    def make(self, args, params, attrs):
        raise NotImplementedError()


class SvgNode(Node):
    def make(self, args, params, attrs):
        return load_svg(self.content, attrs.get('width'), attrs.get('height'), fonts=self.manager.fonts_for_svg_loader)


class ImageNode(Node):
    def make(self, args, params, attrs):
        return self.content


class PsdNode(Node):
    def make(self, args, params, attrs):
        self.content.update(attrs)
        return self.content.render()


class SvgManagerNode(Node):
    def make(self, args, params, attrs):
        if args:
            width, height = args
        else:
            width, height = self.manager.svg_manager.parse_args(None)
        content = self.manager.svg_manager.make_svg(self.content, attrs)
        return load_svg(content.encode('utf-8'), width, height, fonts=self.manager.fonts_for_svg_loader)


class FunctionNode(Node):
    node_marker = '<<'
    re_var = r'\$\$([^\W0-9]\w*)[\^]?'

    def __init__(self, manager, name, args, params, body):
        super().__init__(manager, body)
        self.name = name
        self.args = args
        self.params = params

    def trans_var(self, s, params):
        if s.startswith(self.node_marker):
            return self.manager.make_image(s[len(self.node_marker):])
        return yaml.loads(re.sub(self.re_var, lambda x: str(params[x.group(1)]), s))

    def _translate_list(self, params, data):
        result = []
        for item in data:
            if isinstance(item, str):
                item = self.trans_var(item, params)
            result.append(item)
        return result

    def _translate_map(self, params, data):
        result = {}
        for k, v in data.items():
            if isinstance(v, str) and v:
                v = self.trans_var(v, params)
            if v is not None:
                result[k] = v
        return result

    module_image_operations = (
        (f'{__name__}.operations.image', False),
        f'{__name__}.operations.array',
        'skimage',
        'numpy',
        ('PIL.ImageOps', False)
    )

    def make(self, args, params, attrs):
        params = {**self.params, **params}
        image = None
        for index, (name, value) in enumerate(self.content.items()):
            value = value or {}
            value = value.copy()
            if index == 0:
                node = self.manager.get_node(name)
                image = node.make(self._translate_list(params, self.args), params, self._translate_map(params, value))
            else:
                name = name.rstrip('+')
                args = value.pop('$', None) or []
                func = None
                is_na = True
                for m in self.module_image_operations:
                    if isinstance(m, str):
                        is_na = True
                    else:
                        m, is_na = m
                    try:
                        func = get_module_attr(f'{m}.{name}')
                        break
                    except (ModuleNotFoundError, AttributeError):
                        pass
                if func is None:
                    is_na = False
                    func = getattr(Image.Image, name, None)
                if func is None:
                    raise AttributeError(f"Can't find func: {name}")
                if is_na:
                    if isinstance(image, Image.Image):
                        image = pil_to_ndarray(image)
                else:
                    if not isinstance(image, Image.Image):
                        image = ndarray_to_pil(image)
                image = func(image, *self._translate_list(params, args), **value)

        if not isinstance(image, Image.Image):
            return ndarray_to_pil(image)
        return image


class Manager:
    ignore_file = '.designignore'
    entry_marker = '>>'
    dump_ext = '.png'
    function_node_cls = FunctionNode
    svg_node_cls = SvgNode
    image_node_cls = ImageNode
    psd_node_cls = PsdNode
    svg_manager_node_cls = SvgManagerNode
    svg_manager_cls = SvgManager
    net_req_design_cls = NetReqDesign

    def __init__(self, path=None):
        self.path_cache = path
        self.net_req_design = self.net_req_design_cls()
        self.svg_manager = self.svg_manager_cls()
        self.setup = OrderedDict()
        self.entry_names = []
        self.function_map = {}
        self.svg_map = {}
        self.font_map = {}
        self.image_map = {}
        self.psd_map = {}

    async def dump(self, path):
        sure_dir(path)
        for image_name, image_data in self.setup.items():
            data_fetch = image_data.get('fetch')
            if data_fetch:
                for request_name, args_list in data_fetch.items():
                    for args in args_list:
                        data_result = await self.net_req_design.request(request_name, args)
                        for (name, params) in data_result:
                            image = self.make_image(image_name, params=params)
                            image.save(os.path.join(path, name + self.dump_ext))
            data_static = image_data.get('static')
            if data_static:
                for name, params in data_static.items():
                    image = self.make_image(image_name, params=params)
                    image.save(os.path.join(path, name + self.dump_ext))

    def entries(self, args=None, params=None, attrs=None):
        for name in self.entry_names:
            yield name, self.make_image(name, args, params, attrs)

    def make_image(self, name, args=None, params=None, attrs=None):
        if self.path_cache:
            path_target = os.path.join(self.path_cache, name + self.dump_ext)
            if os.path.isfile(path_target):
                return Image.open(path_target)
        return self.get_node(name).make(args, params or {}, attrs or {})

    def get_node(self, name):
        return self.function_map.get(name) or \
            self.new_svg_node(name) or \
            self.new_image_node(name) or \
            self.new_psd_node(name) or \
            self.new_svg_manager_node(name)  # always at end

    def new_svg_node(self, name):
        path = self.svg_map.get(name)
        if path:
            return self.svg_node_cls(self, read_file(path))

    def new_image_node(self, name):
        path = self.image_map.get(name)
        if path:
            return self.image_node_cls(self, Image.open(path))

    def new_psd_node(self, name):
        path = self.psd_map.get(name)
        if path:
            return self.psd_node_cls(self, PsdCanvas.load(path))

    def new_svg_manager_node(self, name):
        return self.svg_manager_node_cls(self, name)

    @property
    def all_font_map(self):
        return {**self.svg_manager.font_map, **self.font_map}

    @property
    def fonts_for_svg_loader(self):
        return {k: {'font_path': v} for k, v in self.all_font_map.items()}

    def load_data(self, data_map):
        data_setup = data_map.pop('setup', None)
        if data_setup:
            dict_merge(self.setup, data_setup)
        data_fetch = data_map.pop('fetch', None)
        if data_fetch:
            self.load_data_fetch(data_fetch)
        for name, body in data_map.items():
            body = body.copy()
            args = body.pop('$', None) or []
            params = body.pop('$$', None) or {}
            if name.endswith(self.entry_marker):
                name = name[:len(name) - len(self.entry_marker)]
                self.entry_names.append(name)
            self.function_map[name] = self.function_node_cls(self, name, args, params, body)

    def load_data_fetch(self, data_map):
        self.net_req_design.load_body_data(data_map)

    def load_file_yaml(self, path):
        self.load_data(yaml.load(path))

    def load_file_svg(self, path):
        name = os.path.splitext(os.path.basename(path))[0]
        self.svg_map[name] = path

    def load_file_psd(self, path):
        name = os.path.splitext(os.path.basename(path))[0]
        self.psd_map[name] = path

    def load_file_rp(self, path):
        self.net_req_design.load_rp(path)

    def load_file_font(self, path):
        name = os.path.splitext(os.path.basename(path))[0]
        self.font_map[name] = path

    def load_file_image(self, path):
        name = os.path.splitext(os.path.basename(path))[0]
        self.image_map[name] = path

    def load_path(self, *paths):
        def walk(fp, match, _):
            if match:
                return
            ext = os.path.splitext(fp)[-1].lower()
            if ext == '.svg':
                self.load_file_svg(fp)
            elif ext == '.yaml':
                self.load_file_yaml(fp)
            elif ext == '.psd':
                self.load_file_psd(fp)
            elif ext == '.rp':
                self.load_file_rp(fp)
            elif ext in font_extensions:
                self.load_file_font(fp)
            elif ext in image_extensions:
                self.load_file_image(fp)

        for path in paths:
            self.svg_manager.load_path(path)
            FileHitChecker(path, self.ignore_file).walk(walk)
