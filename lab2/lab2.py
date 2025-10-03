import unittest

def diap(d1, d2):
    massive = []
    for i in range(min(d1, d2), max(d1, d2) + 1):
        massive.append(i)
    return massive

def guess_number(target, lst, type='seq') -> list[int, int | None]:
    if type == 'bin':
        left, right = 0, len(lst) - 1
        guess = 0
        while left <= right:
            mid = (right + left) // 2
            if lst[mid] == target:
                return [lst[mid], guess]
            else:
                guess += 1
                if lst[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return [None, guess]  # Если не нашли
    else:
        # Последовательный поиск
        for i, val in enumerate(lst):
            if val == target:
                return [val, i]
        return [None, None]

def main():
    target = int(input('Введите число: '))
    start_range = int(input('Введите начало диапазона: '))
    end_range = int(input('Введите конец диапазона: '))
    d = list(range(start_range, end_range + 1))
    result_seq = guess_number(target, d, type='seq')
    result_bin = guess_number(target, d, type='bin')
    print(f"Результат последовательного поиска: {result_seq}")
    print(f"Результат бинарного поиска: {result_bin}")

if __name__ == '__main__':
    main()


#
# def main():
#     """
#     Ввод значений с клавиатуры для формирования
#     списка, по которому мы ищем искомое число и
#     искомого числа
#
#     __вызов функции guess-number с параметрами: __
#       - искомое число (target)
#       - список, по-которому идем
#       - тип поиска (последовательный, бинарный)
#
#     __вывод результатов на экран__
#     :return:
#     """
#
#     target = int(input('Введите target'))
#     start_range = int(input('Введите начало диап'))
#     end_range = int(input('Введите конец диап'))
#     d = list(range(start_range, end_range + 1))
#
#     def guess_number(target, lst, type='seq') -> list[int, int | None]:
#         if type == 'bin':
#             left, right = 0, len(lst)
#             guess = 0
#             while left < right:
#                 mid = (right + left) // 2
#                 if lst[mid] == target:
#                     return lst[mid], guess
#                 else:
#                     guess += 1
#                     if lst[mid] < target:
#                         left = mid
#                     else:
#                         right = mid
#
# def guess_number(target, lst, type='seq') -> list[int, int | None]:
#     if type == 'seq':
#         # ищем число последовательно
#         ...
#     elif type == 'bin':
#         # ищем число с помощью алгоритма бинарного поиска
#         ...
#
#     return [10, 1]
#
#
# if __name__ == '__main__':
#     pass
    # main() res = guess_number(target, d, type='bin')
    #     print(f'{res}')