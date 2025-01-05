from dektools.design.res.base import ResBase, ResText
from dektools.ext.font import font_extensions
from deknetreq.design.apply import ResYamlNet, ResRp
from .base import res_types


@res_types.register
class SvgYamlRes(ResYamlNet):
    ext = ['.svg', '.yaml']


@res_types.register
class SvgEmbedRes(ResText):
    ext = '.svg'


@res_types.register
class RpRes(ResRp):
    pass


@res_types.register
class FontRes(ResBase):
    ext = font_extensions
