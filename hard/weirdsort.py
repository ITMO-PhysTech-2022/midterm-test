import random

from pytest import mark


def weirdsort(ids):
    """
    Дан массив строчек вида 'yyy xxx', где x - буквы латинского алфавита, а y - цифры
    Отсортируйте массив в порядке возрастания строк xxx в алфавитном порядке БЕЗ
    УЧЕТА РЕГИСТРА, а при равенстве - по возрастанию чисел yyy

    weirdsort(['012 xAb', '012 yAb', '999 Xab']) :returns ['012 xAb', '999 Xab', '012 yAb']
    """
    pass


@mark.parametrize('data', [
    [[], []],
    [['111 xxx'], ['111 xxx']],
    [['012 xAb', '012 yAb', '999 Xab'], ['012 xAb', '999 Xab', '012 yAb']],
    [['111 xxx', '111 xxx'], ['111 xxx', '111 xxx']],
    [['123 abc', '122 AbB', '121 abB', '121 aBC', '321 ABb'],
     ['121 abB', '122 AbB', '321 ABb', '121 aBC', '123 abc']]
])
def test_weirdsort(data):
    assert weirdsort(data[0]) == data[1]


@mark.parametrize('seed', list(range(50)))
def test_randomized(seed):
    random.seed(seed)
    n = 200
    words, nums = [], []
    for i in range(n):
        w = ''
        for i in range(3):
            c = str(random.randint(ord('a'), ord('z')))
            w += c
        words.append(w)
        nums.append(f'{random.randint(0, 999)}:0>3')

    words.sort()
    nums.sort()
    for i in range(len(words)):
        for j in range(3):
            if random.uniform(0, 1) < 0.5:
                words[i] = words[i][:j] + words[i][j].upper() + words[i][j + 1:]
    items = [f'{nums[i]} {words[i]}' for i in range(n)]
    citems = items[:]
    random.shuffle(items)
    assert weirdsort(items) == citems