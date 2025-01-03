#!/usr/bin/env python
# -*-coding:utf-8 -*-

import pytest
from eopt import Objective
from eopt import Variable


def test_Objective():
    obj = Objective()
    assert type(obj) == Objective

    x = 1
    obj = Objective(x**2)
    assert obj(3) == 1
    
    x = 1
    obj = Objective(lambda x:x**2)
    assert obj(3) == 9
    assert obj(7) == 49

    obj = Objective(lambda x,y:x**2+y)
    assert obj(3, 1) == 10
   
    def test_var(x,y):
        return sum(x) + sum(y)
 
    obj = Objective(test_var)
    assert obj([3], [1]) == 4

def test_Objective_var():
    x = Variable(1)
    obj = Objective(x**2)
    x.set_value(3)
    assert obj() == 1

    # assert obj.get_value == 9


def test_Variable_init():
    var = Objective(init=0)
    var = Objective()
    assert var._value == 0

    var._value = 1
    assert var._value == 1