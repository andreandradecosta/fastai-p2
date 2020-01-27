from nb_00 import *
import operator

def test(a, b, cmp, cname=None):
    if cname is None: cname = cmp.__name__
    assert cmp(a, b), f'{cname}:\n{a}\n{b}'

def test_ep(a, b): test(a, b, operator.eq, '==')