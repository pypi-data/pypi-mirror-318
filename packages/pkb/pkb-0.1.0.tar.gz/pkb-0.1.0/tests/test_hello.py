import pytest 

from hello import main

def test_main():
    x = 'xxx'
    y = main(x)
    assert x == y