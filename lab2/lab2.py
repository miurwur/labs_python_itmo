def diap(d1, d2):
    '''
    Создает список чисел в диапазоне от минимального до максимального из двух переданных чисел
    d1 (int): Первое число диапазона.
    d2 (int): Второе число диапазона.
    Возвращает список целых чисел (massive) от min(d1, d2) до max(d1, d2) включительно.
    '''
    massive = []
    for i in range(min(d1, d2), max(d1, d2) + 1):
        massive.append(i)
    return massive

def guess_number(target, lst, type='seq'):
    '''
    Производит поиск числа в списке с помощью последовательного или бинарного поиска.
    target (int): число, которое нужно найти.
    lst: список чисел.
    type (str): тип поиска.
    'seq' - последовательный поиск,
    'bin' - бинарный поиск
    Возвращает: [найденное число или None, количество попыток поиска]
    '''
    if type == 'bin':
        ''' Бинарный поиск '''
        left, right = 0, len(lst) - 1
        guess = 0
        while left <= right:
            mid = (right + left) // 2
            if lst[mid] == target:
                return ["Ваше число: ",lst[mid], "Количество сравнений: ", guess]
            else:
                guess += 1
                if lst[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return [None, "Количество сравнений: ", guess]
    else:
        ''' Последовательный поиск '''
        guess = 0
        for i in range(len((lst))):
            if lst[i] == target:
                return ["Ваше число: ",lst[i], "Количество сравнений: ",guess]
            else:
                guess+=1
        return [None, "Количество сравнений: ", guess]

def main():
    target = int(input('Введите число: '))
    start_range = int(input('Введите начало диапазона: '))
    end_range = int(input('Введите конец диапазона: '))
    d = list(range(start_range, end_range + 1))
    result_seq = guess_number(target, d, type='seq')
    result_bin = guess_number(target, d, type='bin')
    print('Результат последовательного поиска: ', result_seq)
    print('Результат бинарного поиска: ', result_bin)

# if __name__ == '__main__':
#     main()

# print(guess_number(6, [1,2,3,4,5,6,7,8,9]))
print(guess_number(1, (), type="bin"))
