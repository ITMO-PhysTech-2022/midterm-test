import random

from pytest import mark


def subsets(n):
    """
    Дано целое неотрицательное число n
    Вернуть массив из всех подмножеств чисел от 1 до n в алфавитном порядке
    Каждое подмножество должно быть возвращено в виде массива (см. примеры)

    subsets(2) :returns [
        [],
        [1],
        [1, 2],
        [2]
    ]
    subsets(3) :returns [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 3],
        [2],
        [2, 3],
        [3]
    ]
    """
    pass


@mark.parametrize('data', [
    [0, [[]]],
    [1, [[], [1]]],
    [2, [[], [1], [1, 2], [2]]],
    [3, [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]],
    [4, [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 4], [1, 3], [1, 3, 4],
         [1, 4], [2], [2, 3], [2, 3, 4], [2, 4], [3], [3, 4], [4]]]
])
def test_subsets(data):
    assert subsets(data[0]) == data[1]


@mark.parametrize('n', list(range(5, 12)))
def test_large(n):
    res = subsets(n)
    expected_len = 2 ** n
    assert len(res) == expected_len
    full = set(range(1, n + 1))
    for item in res:
        assert set(item) | full == full
    for i in range(1, len(res)):
        assert res[i - 1] < res[i]
