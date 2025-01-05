import re
from ...base import TypeBase, TypesBase
from ...res.base import ResBase, ResManager
from ....yaml import yaml


class NodeBase(TypeBase):
    _cls_suffix = 'Node'

    def __init__(self, manager: 'NodeManager', res: ResBase):
        self.manager = manager
        self.res = res

    def make(self, args, params, attrs):
        raise NotImplementedError()


class MixinTrans:
    assign_marker = '<<'
    re_var = r'\$\$([^\W0-9]\w*)[\^]?'

    def trans_var(self, s, params):
        if s.startswith(self.assign_marker):
            return self._translate_assign(s[len(self.assign_marker):], params)
        return yaml.loads(re.sub(self.re_var, lambda x: str(params[x.group(1)]), s))

    def _translate_assign(self, s, params):
        pass

    def translate_list(self, params, data):
        result = []
        for item in data:
            if isinstance(item, str):
                item = self.trans_var(item, params)
            result.append(item)
        return result

    def translate_map(self, params, data):
        result = {}
        for k, v in data.items():
            if isinstance(v, str) and v:
                v = self.trans_var(v, params)
            if v is not None:
                result[k] = v
        return result


class NodeTypes(TypesBase):
    pass


class NodeManager:
    types: NodeTypes = None

    def __init__(self, res_manager: ResManager):
        self.res_manager = res_manager

    def load_path(self, *paths):
        self.res_manager.load_path(*paths)

    def get_node(self, name):
        res = self.res_manager.find_res(name)
        node_cls = None
        if isinstance(res, self.res_manager.unknown_res_cls):
            node_cls = self.types.get(res.name)
        if node_cls is None:
            typed = res.get_typed()
            node_cls = self.types[typed]
        return node_cls(self, res)
