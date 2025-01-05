from dektools.design.base import split_function
from .base import NodeCanvas, NodeSvg, node_types
from .elements import *


@node_types.register
class FunctionNode(NodeCanvas):
    def make(self, args, params, attrs):
        _args, _params, body = self.res.content
        wh = args
        if not wh:
            wh = _args or []
        if len(wh) == 0:
            wh.append(self.manager.default_width)
        if len(wh) == 1:
            wh.append(self.manager.default_height)
        params = {**_params, **params}
        result = ""
        for key, value in body.items():
            _args, _params, _body = split_function(value)
            name, trans = self.manager.parse_call_label(params, key, self)
            node = self.manager.get_node(name)
            if isinstance(node, NodeCanvas):
                node.set_wh(*wh)
            content = node.make(_args,
                                {**params, **self.manager.translate_map(params, _params)},
                                self.manager.translate_map(params, _body))
            result += f"""<g{trans}>{content}</g>""" if trans or node.need_g_wrapper else content
        return result


@node_types.register
class SvgEmbedNode(NodeSvg):
    need_g_wrapper = True

    def make(self, args, params, attrs):
        if attrs:
            return self.manager.render_by_struct({'g': {**attrs, '+': self.res.content}}, params)
        return self.res.content


@node_types.register
class UnknownNode(NodeSvg):
    def make(self, args, params, attrs):
        return self.manager.render_by_struct({self.res.name: attrs}, params)
