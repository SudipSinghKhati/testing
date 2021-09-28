import pytest


def fun(x):
    return x + 5


def test_method():
    assert fun(3) == 8
