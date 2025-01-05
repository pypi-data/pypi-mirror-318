from PIL import Image
from skimage.io._plugins.pil_plugin import pil_to_ndarray, ndarray_to_pil
from dektools.module import get_module_attr
from dektools.design.base import split_function
from ...svg.load import load_svg
from .base import NodeImage, node_types
from ..res import get_fonts


@node_types.register
class FunctionNode(NodeImage):
    module_image_operations = (
        (f'{__name__}.operations.image', False),
        f'{__name__}.operations.array',
        'skimage',
        'numpy',
        ('PIL.ImageOps', False)
    )

    def make(self, args, params, attrs):
        _args, _params, body = self.res.content
        args = _args or args
        params = {**_params, **params}
        image = None
        for index, (name, value) in enumerate(body.items()):
            _args, _params, _body = split_function(value)
            args = _args or args
            params = {**_params, **params}
            if index == 0:
                node = self.manager.get_node(name)
                image = node.make(
                    self.manager.translate_list(params, args),
                    params,
                    self.manager.translate_map(params, _body))
            else:
                name = name.rstrip('+')
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
                image = func(image, *self.manager.translate_list(params, args), **_body)

        if not isinstance(image, Image.Image):
            return ndarray_to_pil(image)
        return image


@node_types.register
class SvgNode(NodeImage):
    def make(self, args, params, attrs):
        return load_svg(self.res.content, attrs.get('width'), attrs.get('height'),
                        fonts=get_fonts(self.manager.res_manager))


@node_types.register
class ImageNode(NodeImage):
    def make(self, args, params, attrs):
        return self.res.content


@node_types.register
class PsdNode(NodeImage):
    def make(self, args, params, attrs):
        self.res.content.update(attrs)
        return self.res.content.render()


@node_types.register
class UnknownNode(NodeImage):
    def make(self, args, params, attrs):
        content = self.manager.svg_manager.make_svg(self.res.name, args, params=attrs)
        return load_svg(content, params.get('width'), params.get('height'), fonts=get_fonts(self.manager.res_manager))
