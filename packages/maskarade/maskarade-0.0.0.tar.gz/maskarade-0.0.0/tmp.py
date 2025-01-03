from abc import ABC, abstractmethod
from functools import partial
from json import dumps
from typing import Any

from maskarade.connector import EventChannel, ModelConnector
from maskarade.manager import ModelsManager
from maskarade.model import ModelBase, model_ref_associations
from maskarade.reference import ModelRef
from maskarade.utils import final_models, make_model_class, model_from_ref


class CascadeCache(ModelBase):
    cascade_enabled: ModelRef
    cascade_min_sp: ModelRef
    cascade_max_sp: ModelRef


class BasicCacheRef(ModelRef, ABC):
    @abstractmethod
    def __init__(self, actuator: str, control: str, variable: str, value_type: type):
        if control != '':
            control = f'{control}:'
        super().__init__(value_type, f'{{actuator}}:basic:{control}{{variable}}',
                         model_ref_fmt_args={'actuator': actuator, 'variable': variable})


class BasicEnableCacheRef(BasicCacheRef):
    def __init__(self, actuator: str, control: str = ''):
        super().__init__(actuator, control, 'enable', bool)


class BasicSPCacheRef(BasicCacheRef):
    def __init__(self, actuator: str, control: str = ''):
        super().__init__(actuator, control, 'sp', float)


class BasicCache(ModelBase):
    basic_enabled: BasicEnableCacheRef
    basic_sp: BasicSPCacheRef

    basic_cd_enabled: BasicEnableCacheRef
    basic_cd_sp: BasicSPCacheRef

    basic_cp_enabled: BasicEnableCacheRef
    basic_cp_sp: BasicSPCacheRef


class AgitationCache(BasicCache, CascadeCache, final=True):
    pv: int

    basic_enabled = BasicEnableCacheRef('agitation')
    basic_sp = BasicSPCacheRef('agitation')

    basic_cd_enabled = BasicEnableCacheRef('agitation', 'cd')
    basic_cd_sp = BasicSPCacheRef('agitation', 'cd')

    basic_cp_enabled = BasicEnableCacheRef('agitation', 'cp')
    basic_cp_sp = BasicSPCacheRef('agitation', 'cp')

    cascade_enabled = ModelRef(bool, 'agitation:cascade:enabled')
    cascade_min_sp = ModelRef(int, 'agitation:cascade:min_sp')
    cascade_max_sp = ModelRef(int, 'agitation:cascade:max_sp')


class DpCache(BasicCache, final=True):
    DpBasicEnableCacheRef = partial(BasicEnableCacheRef, 'dp')
    DpBasicSpCacheRef = partial(BasicSPCacheRef, 'dp')

    basic_enabled = DpBasicEnableCacheRef()
    basic_sp = DpBasicSpCacheRef()

    basic_cd_enabled = DpBasicEnableCacheRef('cd')
    basic_cd_sp = DpBasicSpCacheRef('cd')

    basic_cp_enabled = DpBasicEnableCacheRef('cp')
    basic_cp_sp = DpBasicSpCacheRef('cp')


# Para gestion genral de gases bombas analog y demas
stirrer: type[BasicCache] = AgitationCache.as_type(BasicCache)
if stirrer:
    print('stirrer: Is basic cache')
else:
    print('stirrer: Not a basic cache')

dp: type[DpCache] = DpCache.as_type(CascadeCache)
if dp:
    print('dp: Is cascade cache')
else:
    print('dp: Not a cascade cache')


class GasCacheBase(BasicCache):
    _gas_id: int

    basic_enabled = BasicEnableCacheRef('gas:line{gas_id}', )
    basic_sp = BasicSPCacheRef('gas:line{gas_id}')
    basic_cd_enabled = BasicEnableCacheRef('gas:line{gas_id}', 'cd')
    basic_cd_sp = BasicSPCacheRef('gas:line{gas_id}', 'cd')
    basic_cp_enabled = BasicEnableCacheRef('gas:line{gas_id}', 'cp')
    basic_cp_sp = BasicSPCacheRef('gas:line{gas_id}', 'cp')

    @property
    def gas_id(self):
        return self._gas_id


def make_gas_cache_class(gas_id: int) -> type[GasCacheBase]:
    cls = make_model_class('Gas{gas_id}Cache', GasCacheBase, gas_id=gas_id)
    cls._gas_id = gas_id
    return cls


Gas1Cache = make_gas_cache_class(1)
Gas2Cache = make_gas_cache_class(2)


class VoidConnector(ModelConnector):

    def get_value(self, model_ref: str) -> Any:
        pass

    def set_value(self, model_ref: str, value: Any) -> None:
        pass

    def send_event(self, channel: EventChannel, payload: Any) -> None:
        pass

    def receive_event(self) -> tuple[EventChannel, Any]:
        pass


class JsonModelsManager(ModelsManager):
    def gen_tree(self) -> dict[str, dict]:
        association = model_ref_associations()
        tree = {}
        for ref, (model, model_ref) in association.items():
            if model not in self._models:
                continue

            parts = ref.split(':')
            current_level = tree
            for i, part in enumerate(parts):
                if i == len(parts) - 1:
                    current_level[part] = model_ref.value_type.__name__
                    continue
                if part not in current_level:
                    current_level[part] = {}
                current_level = current_level[part]
        return tree


connector = VoidConnector()
a = final_models(GasCacheBase)
a.pop()
mm = JsonModelsManager(a, connector)

# Para los eventos sin siquiera instanciar la clase
cc = model_from_ref('dp:basic:cd:enable')
if issubclass(cc, DpCache):
    print('cache: Is dp cache')
else:
    print('cache: Not a dp cache')

cc = model_from_ref('gas:line1:basic:cd:enable')
if issubclass(cc, Gas1Cache):
    print('cache: Is GAS 1')
else:
    print('cache: not is GAS 1')

tree = mm.gen_tree()
print(dumps(tree, indent=4))
