import pytest
from File1 import minimum, maximum, summa, product, mydata, mydata2
import math
from functools import partial
from timeit import timeit


def test_minimum_good():
    assert minimum(mydata) == min(mydata)


def test_maximum_good():
    assert maximum(mydata) == max(mydata)


def test_summa_good():
    assert summa(mydata) == sum(mydata)


def test_product_good():
    assert product(mydata) == math.prod(mydata)


def test_time_check():
    assert timeit(partial(summa, mydata), number=1) < timeit(partial(summa, mydata2), number=1)


@pytest.mark.parametrize("data, expected_result", [([1, 2, 3], 6), ([1, 2, 3, 4, 5], 15)])
def test_myrandomtest(data, expected_result):
    assert summa(data) == expected_result
