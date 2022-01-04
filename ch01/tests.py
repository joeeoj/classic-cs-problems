import pytest

from fib import fib_fail, fib_success
from fib import fib_memo, fib_memo_improved
from fib import fib_non_recursive


def test_infinite_loop():
    with pytest.raises(RecursionError):
        fib_fail(4)


def test_zero():
    assert fib_success(0) == 0


def test_one():
    assert fib_success(1) == 1


def test_success():
    assert fib_success(4) == 3
    assert fib_success(8) == 21


def test_large_number():
    assert fib_memo(50) == 12_586_269_025


def test_another_large_number():
    assert fib_memo_improved(60) == 1_548_008_755_920


def test_non_recursive():
    """combination of all previous tests"""
    assert fib_non_recursive(0) == 0
    assert fib_non_recursive(1) == 1
    assert fib_non_recursive(4) == 3
    assert fib_non_recursive(50) == 12_586_269_025
    assert fib_non_recursive(60) == 1_548_008_755_920
