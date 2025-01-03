import copy
import numpy as np
from ..common import *
import pyomo.environ as pyo



class VariableBase:
    def __init__(self, *shape, **kwargs):
        if shape:
            if isinstance(shape, tuple) and len(shape):
                if not is_single_level_tuple(shape):
                    self.shape = shape[0]
                else:
                    self.shape = shape
            if isinstance(self.shape, int):
                self.shape = (self.shape,)
        else:
            self.shape = None
        self.lb = kwargs.pop('lb', -np.inf)
        self.ub = kwargs.pop('ub', np.inf)
        self.name = kwargs.pop('name', "")
        self.value = kwargs.pop('value', 0)
        self.type = "B"
        
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __add__(self, other):
        if isinstance(other, VariableBase):
            return VariableBase(self.value + other.value)
        return NotImplemented

    def set_value(self, value):
        self._value = value

    def to_pyomo(self):
        return pyo.Var(within=pyo.NonNegativeReals)
        
    def __eq__(self, other):
        if isinstance(other, VariableBase):
            return self.value == other.value
        return NotImplemented

    # 特殊方法：长度运算
    def __len__(self):
        return 1

    # 特殊方法：迭代
    def __iter__(self):
        return iter([self.value])

    # 特殊方法：一元运算
    def __neg__(self):
        return VariableBase(-self.value)

    # 特殊方法：反算术运算
    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        return 1 / self.__truediv__(other)

    # 特殊方法：算术运算
    def __add__(self, other):
        if isinstance(other, VariableBase):
            return Variable(init_value=self.value + other.value, vtype=self.type)
        if isinstance(other, (int, float)):
            return Variable(init_value=self.value + other, vtype=self.type)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, VariableBase):
            return Variable(init_value=self.value - other.value)
        if isinstance(other, (int, float)):
            return Variable(init_value=self.value - other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, VariableBase):
            return Variable(init_value=self.value * other.value, vtype=self.type)
        if isinstance(other, (int, float)):
            return Variable(init_value=self.value * other, vtype=self.type)
        return NotImplemented

    def __pow__(self, other, modulo=None): 
        try:
            if isinstance(other, VariableBase):
                result = Variable(self._value ** other.value)
            else:
                result = Variable(self._value ** other)
            if modulo is not None:
                result %= modulo
            return result
        except Exception as e:
            return NotImplemented
        
    def check_le(self, value):
        violate = self.value - value
        if violate > 0:
            return violate
        return np.array([0])

    def __lt__(self, other):
        return self.__le__(other)
    
    def __le__(self, other):
        if isinstance(other, VariableBase):
            return self.check_le(other.value)
        if isinstance(other, (int, float)):
            return self.check_le(other)
        return NotImplemented


    def __gt__(self, other):
        return self.__ge__(other)
    
    def check_ge(self, value):
        violate = value - self.value
        if violate > 0:
            return violate
        return np.array([0])
        
    def __ge__(self, other):
        if isinstance(other, VariableBase):
            return self.check_ge(other.value)
        if isinstance(other, (int, float)):
            return self.check_ge(other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, VariableBase):
            return Variable(self.value / other.value)
        return NotImplemented


    # 特殊方法：获取对象的字符串表示
    def __str__(self):
        return f"VariableBase with value: {self.value}"

    # 特殊方法：获取对象的详细字符串表示
    def __repr__(self):
        return f"VariableBase(value={self.value})"

    def __deepcopy__(self, memo):
        new_instance = Variable(**self.__dict__)
        return new_instance



def Variable(*args, **kwargs):
    # Pretend to be a class
    vtype = kwargs.pop('vtype', "C")
    if len(vtype) == 1:
        vtype = vtype_map.get(vtype, vtype)
    vtype = vtype.lower()
    try:
        return VARIABLES.module_dict[vtype](*args, **kwargs)
    except Exception as e:
        raise ValueError(f"Unsupported type: {vtype}") from e

def is_single_level_tuple(obj):
    if isinstance(obj, tuple):
        return all(not isinstance(elem, tuple) for elem in obj)
    return False


@VARIABLES.register_module()
class Continuous(VariableBase):
    # def __new__(cls, 
    #             *shape  , 
    #         **kwargs):
    #     if not shape:
    #         shape = (1,)
    #     if not is_single_level_tuple(shape):
    #         shape = shape[0]
    #     dtype=kwargs.pop('dtype', float)
    #     buffer=kwargs.pop('buffer', None)
    #     offset=kwargs.pop('offset', 0)
    #     strides=kwargs.pop('strides', None)
    #     order=kwargs.pop('order', None)
    #     # obj = np.ndarray(*shape, 
    #     #             dtype=dtype)
    #     # super(np.ndarray, cls).__init__(shape, 
    #     #             dtype=dtype, 
    #     #             buffer=buffer, 
    #     #             offset=offset,
    #     #             strides=strides, 
    #     #             order=order)
    #     return super(Continuous, cls).__new__(cls, shape, dtype=dtype)

    def __init__(self, 
            *shape  , 
            **kwargs
            ):
        VariableBase.__init__(self, *shape, **kwargs)
        self.type = "C"
        init_value = kwargs.pop('init_value', 0)
        self.init_value(init_value)

    def uniform(self, init_value=None):
        if init_value is not None:
            return np.random.random(self.shape)
        else:
            lb = self.lb if self.lb != -np.inf else -99999999
            ub = self.ub if self.ub != np.inf else 99999999
            return np.random.uniform(lb, ub, size=self.shape)

    def init_value(self, value):
        if value is not None:
            if not hasattr(value, "shape"):
                value = np.array(value)
            print(value)
            if self.shape and hasattr(value, "shape") and self.shape != value.shape:
                raise ValueError(f"The initial value must be the same as the set shape {self.shape}")
            self.value = value
        else:
            lb = self.lb if self.lb != -np.inf else -99999999
            ub = self.ub if self.ub != np.inf else 99999999
            self.value = np.random.uniform(lb, ub, size=self.shape)

    # def get_shape(self, value):
    #     shape = len(self.init_value())
    #     if isinstance(self.shape, tuple):
    #         init_shape = value.shape
    #     if init_shape != self.shape:
    #         raise ValueError(f"error shape for init shape : {init_shape} and shape {self.shape}") from None
    #     return shape

    def check(self, value):
        if not isinstance(value, (np.ndarray) ):
            return False
        if value < self.lb:
            return False
        if value > self.ub:
            return False
        if self.shape != value.shape:
            return False
        if not np.isscalar(value):
            return False
        return True



