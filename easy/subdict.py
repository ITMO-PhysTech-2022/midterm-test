import random

from pytest import mark


def subdict(d1, d2):
    """
    Даны два словаря d1 и d2, требуется проверить, что первый является
    "под-словарем" второго, то есть не имеет ключей, отсутствующих в d2,
    а значения, соответствующие одинаковым ключам, в них тоже одинаковы

    subdict({'name': 'Dan'}, {'name': 'Dan', 'age': 22}) :returns True
    subdict({'name': 'Dan'}, {'age': 22}) :returns False
    subdict({'name': 'Dan'}, {'name': 'Darya'}) :returns False
    """
    pass


@mark.parametrize('data', [
    [{'name': 'Dan'}, {'name': 'Dan', 'age': 22}, True],
    [{'name': 'Dan'}, {'name': 'Daniil', 'age': 22}, False],
    [{'name': 'Dan', 'age': 22}, {'name': 'Dan'}, False],
    [{}, {}, True],
    [{'name': 'Dan', 'age': 23}, {'name': 'Dan', 'age': 22}, False],
])
def test_manual(data):
    assert subdict(data[0], data[1]) == data[2]


@mark.parametrize('seed', list(range(20)))
def test_randomized(seed):
    random.seed(seed)
    x, y = {}, {}
    for i in range(100):
        key = random.randint(1, 10 ** 9)
        x[key] = [random.randint(1, 100)]
        y[key] = x[key]
    assert subdict(x, y)
    y[-1] = 100
    assert subdict(x, y)
    x[-1] = 99
    assert not subdict(x, y)
    x[-1] = 100
    assert subdict(x, y)
    x[-2] = 100
    assert not subdict(x, y)
