"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
На вход получаем строку, нужно разрезать ее на 2 равные части и вернуть их
по отдельности. Если длина строки - нечетное число,
то первая часть должна быть больше на 1 символ

Задачу можно решить 2 способами:
    - используя math
    - используя операторы

ПРИМЕРЫ
--------------------------------------------------------------------------------
- 'hello world' -> ('Hello ', 'world')
- 'hello' -> ('hel', 'lo')
- 'some' -> ('so', 'me')
"""


def split_to_parts(str_to_split: str) -> tuple:
    """Разделяет строку на 2 части. Если длина строки нечетная, то первая часть
    на один символ больше

    :param str_to_split: строка для разделения

    :return: кортеж с двумя частями
    """
    length = len(str_to_split)
    middle = length // 2 + length % 2
    part_1 = str_to_split[:middle]
    part_2 = str_to_split[middle:]
    return part_1, part_2


if __name__ == '__main__':
    string = input('Введите строку для разбивки: ')
    print(f"Результат: {split_to_parts(string)}")
