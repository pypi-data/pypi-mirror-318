import os
from PIL import Image
from dektools.file import sure_dir
from dektools.design.node.base import NodeBase, NodeTypes, MixinTrans
from deknetreq.design.apply import NodeManagerNet
from ....svg.design import new_svg_manager
from ...res import ImageYamlRes


class NodeImage(NodeBase):
    pass


node_types = NodeTypes()


class ImageManager(NodeManagerNet, MixinTrans):
    types = node_types

    res_cls_setup = ImageYamlRes

    new_svg_manager = lambda x: new_svg_manager()

    dump_ext = '.png'

    def __init__(self, path_cache, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path_cache = path_cache
        self.svg_manager = self.new_svg_manager()

    async def dump(self, path):
        sure_dir(path)
        async for item_name, name, params in self.fetch_items():
            item = self.make_image(item_name, params=params)
            item.save(os.path.join(path, name + self.dump_ext))

    def entries(self, args=None, params=None, attrs=None):
        for name in self.entry_names:
            yield name, self.make_image(name, args, params, attrs)

    def _translate_assign(self, s, params):
        return self.make_image(s, params=params)

    def make_image(self, name, args=None, params=None, attrs=None):
        if self.path_cache:
            path_target = os.path.join(self.path_cache, name + self.dump_ext)
            if os.path.isfile(path_target):
                return Image.open(path_target)
        return self.get_node(name).make(args or [], params or {}, attrs or {})

    def load_path(self, *paths):
        super().load_path(*paths)
        self.svg_manager.load_path(*paths)
