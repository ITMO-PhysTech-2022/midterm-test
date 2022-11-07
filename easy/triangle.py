import random

from pytest import mark


def triangle(a, b, c):
    """
    Даны три вещественных числа a, b и c
    Требуется проверить, существует ли невырожденный треугольник с такими сторонами

    triangle(1, 2, 3) :returns False
    triangle(2, 3, 4) :returns True
    """
    pass


@mark.parametrize('data', [
    [1, 2, 3, False],
    [2, 3, 4, True],
    [3, 4, 5, True],
    [10, 5, 5, False],
    [0, 100, 100, False],
    [-1, -2, -3, False],
    [55, 16, 57.29, True],
    [11.23, 34.56, 45.78, True],
    [11.23, 34.56, 45.79, False]
])
def test_default(data):
    x = data[:3]
    random.shuffle(x)
    assert triangle(*x) == data[-1]


@mark.parametrize('seed', list(range(20)))
def test_randomized(seed):
    random.seed(seed)
    a = random.randint(1, 10000)
    b = random.randint(1, 10000)
    x, y = [a, b, a + b - 0.1], [a, b, a + b]
    random.shuffle(x)
    random.shuffle(y)
    assert triangle(*x)
    assert not triangle(*y)
    assert not triangle(*[-xi for xi in x])
