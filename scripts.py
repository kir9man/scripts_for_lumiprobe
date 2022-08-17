from collections import Counter
from random import choice


def find_most_letter(string: str) -> tuple:
    """
    Функция возвращает картеж вида:
    (самый часто встречаемый символ, количество повторений)
    Если находится несколько таких символов, возращается случайно выбранный.
    """

    letters = Counter(string.lower()).most_common()
    return choice([answer for answer in letters if answer[1] == letters[0][1]])


def get_sqrt(number: int) -> int | None:
    """
    Возвращает целый квадратный корень переданного числа
    или возвращает None, если корня не существует.
    """
    result = number ** 0.5
    return int(result) if result - int(result) == 0 else None


def test_find_most_letter():
    assert find_most_letter('aaaAAAbc4GGG') == ('a', 6)
    assert find_most_letter('BBBBbbbb') == ('b', 8)
    assert find_most_letter('aaAABBbb') == ('a', 4) or find_most_letter('aaAABBbb') == ('b', 4)
    assert not find_most_letter('Hi, World!!!') == ('!', 2)


def test_get_sqrt():
    assert get_sqrt(25) == 5
    assert get_sqrt(26) is None
    assert get_sqrt(999) is None
    assert get_sqrt(144) == 12
    assert not get_sqrt(143) == 12


test_find_most_letter()
test_get_sqrt()
