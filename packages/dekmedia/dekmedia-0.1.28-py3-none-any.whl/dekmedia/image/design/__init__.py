from .node.base import ImageManager
from .res.base import ImageResManager
from .node import *
from .res import *
from .const import image_ignore_file


def new_image_manager(path_cache=None):
    return ImageManager(path_cache, ImageResManager([image_ignore_file]))
