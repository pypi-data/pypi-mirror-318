from .node.base import SvgManager
from .res.base import SvgResManager
from .node import *
from .res import *
from .const import svg_ignore_file


def new_svg_manager():
    return SvgManager(SvgResManager([svg_ignore_file]))
