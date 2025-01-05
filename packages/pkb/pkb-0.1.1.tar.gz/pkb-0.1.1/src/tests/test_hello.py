import pytest 

from pkb.hello import main

def test_main():
    x = 'xxx'
    y = main(x)
    assert x == y