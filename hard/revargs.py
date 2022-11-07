import random

from pytest import mark


def revargs(f):
    """
    Дана функция f от позиционных аргументов
    Верните функцию, которая делает то же самое, что и f, но с обратным порядком
    аргументов

    : если f(x, y) = x - y, то revargs(f)(x, y) = y - x
    : если f(x, y, z) = x * y / z, то revargs(f)(x, y, z) = z * y / x
    : если f(x, y, z, t) = x, то revargs(f)(x, y, z, t) = t
    """
    pass


def test_example():
    for x, y in [(1, 2), (2, 1), (0, 3), (4, 0)]:
        assert revargs(lambda x, y: x - y)(x, y) == y - x
        assert revargs(lambda x, y: x ** y)(x, y) == y ** x
    y = 'abacaba'
    for x, z in [('12', ''), ('', '()'), ('-', '++')]:
        assert revargs(lambda x, y, z: x + y + z)(x, y, z) == z + y + x


@mark.parametrize('seed', list(range(5)))
def test_0_arguments(seed):
    random.seed(seed)
    res = random.randint(1, 1000)
    assert revargs(lambda: res)() == res


@mark.parametrize('n', list(range(2, 8)))
def test_sum(n):
    random.seed(n)
    f = lambda *args: sum(map(str, args)) if len(args) == n else None
    data = [random.randint(1, 1000) for _ in range(n)]
    rdata = list(reversed(data))
    res = random.randint(1, 1000)
    assert revargs(f)(data) == f(rdata)
