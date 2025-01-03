from .common import *
from .variables import VariableBase
import pyomo.environ as pyo


class Constraint:
    """
    Constraint(rule, name="")
    sense: 
    """
    def __init__(self, 
                 rule: int=1, 
                 ctype: int=1,  # 0 Equality Constraints  1 for Inequality constraints
                 name: str=""):
        if callable(rule):
            self._rule = rule
        elif isinstance(rule, VariableBase):
            raise ValueError(f"Please input function rather than expression")
        else:
            self._rule = lambda *args, **kwargs:rule
        self.name = name
        self.ctype = ctype
        
    @property
    def rule(self):
        return self._rule

    @rule.setter
    def rule(self, value):
        self._rule = value

    def __call__(self, *args, **kwargs):
        return self._rule(*args, **kwargs)

    def to_pyomo(self):
        return pyo.Constraint(rule=self._rule)
