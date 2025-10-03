def diap(d1, d2):
    massive = []
    for i in range(min(d1, d2), max(d1, d2) + 1):
        massive.append(i)
    return massive

def guess_number(target, lst, type='seq'):
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
        guess = 0
        for i in range(len((lst))):
            if lst[i] == target:
                return [lst[i],guess]
            else:
                guess+=1
        return [None, guess]

def main():
    target = int(input('Введите число: '))
    start_range = int(input('Введите начало диапазона: '))
    end_range = int(input('Введите конец диапазона: '))
    d = list(range(start_range, end_range + 1))
    result_seq = guess_number(target, d, type='seq')
    result_bin = guess_number(target, d, type='bin')
    print('Результат последовательного поиска: ', result_seq)
    print('Результат бинарного поиска: ', result_bin)

if __name__ == '__main__':
    main()