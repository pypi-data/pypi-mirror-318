#!/usr/bin/env python
# -*-coding:utf-8 -*-

import numpy as np
import pytest
from eopt import Variable, Continuous


def test_Continuous():
    var = Continuous()
    assert type(var) == Continuous


def test_Continuous_init():
    var = Continuous(init_value=0)
    assert var._value == 0

    var._value = 1
    assert var._value == 1
    
    var = Continuous()
    assert var._value == 0
    assert var.shape == (1,)

    var = Continuous(init_value=[1,2,3])
    assert var._value == [1,2,3]

    var = Continuous(init_value=np.array([1,2,3]))
    assert np.array_equal(var._value, np.array([1,2,3])) 

    var = Continuous(1, init_value=1)
    assert var._value == 1
    assert var.shape == (1,)

    var = Continuous(1,2, init_value=[0,1])
    assert var._value == [0,1]
    assert var.shape == (1,2)

    with pytest.raises(ZeroDivisionError):
        1 / 0
        
    with pytest.raises(ValueError):
        Continuous(1, init_value=[0,1])


def test_Continuous_add():
    var1 = Continuous(init_value=0)
    var2 = Continuous(init_value=2)
    var1 = var1 + var2
    assert var1._value == 2

    var1 = Continuous(init_value=np.array([1,2,3]))
    var2 = Continuous(init_value=np.array([6,7,8]))
    var1 = var1 + var2
    assert np.array_equal(var1._value, np.array([7,9,11])) 

    var1 = Continuous(init_value=np.array([1.0,2.0,3.0]))
    var2 = Continuous(init_value=np.array([6.001,7,8]))
    var1 = var1 + var2
    assert np.array_equal(var1._value, np.array([7.001,9,11])) 

def test_Continuous_sub():
    var1 = Continuous(init_value=0)
    var2 = Continuous(init_value=2)
    var1 = var1 - var2
    assert var1._value == -2

    var1 = Continuous(init_value=np.array([1,2,3]))
    var2 = Continuous(init_value=np.array([6,7,8]))
    var1 = var1 - var2
    assert np.array_equal(var1._value, np.array([-5,-5,-5])) 

def test_Continuous_mul():
    var1 = Continuous(init_value=0)
    var2 = Continuous(init_value=2)
    var1 = var1 * var2
    assert var1._value == 0

    # var1 = Continuous(init_value=np.array([1,2,3]))
    # var2 = Continuous(init_value=np.array([6,7,8]))
    # var1 = var1 - var2
    # assert np.array_equal(var1._value, np.array([-5,-5,-5])) 


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0