from PIL import Image
from dektools.design.res.base import ResBase, ResBytes
from dektools.ext.image import image_extensions
from dektools.ext.font import font_extensions
from deknetreq.design.apply import ResYamlNet, ResRp
from ...psd import PsdCanvas
from .base import res_types


@res_types.register
class ImageYamlRes(ResYamlNet):
    ext = ['.image', '.yaml']


@res_types.register
class SvgRes(ResBytes):
    ext = '.svg'


@res_types.register
class PsdRes(ResBase):
    ext = '.psd'

    def load(self):
        return PsdCanvas.load(self.path)


@res_types.register
class RpRes(ResRp):
    pass


@res_types.register
class ImageRes(ResBase):
    ext = image_extensions

    def load(self):
        return Image.open(self.path)


@res_types.register
class FontRes(ResBase):
    ext = font_extensions


def get_fonts(res_manager):
    fonts = res_manager.get_res_map(FontRes.get_typed()) or {}
    if fonts:
        return {k: {'font_path': v.path} for k, v in fonts.items()}
