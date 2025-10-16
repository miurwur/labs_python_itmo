import collections
def gen_bin_tree(height = 2, root = 6, l_b=lambda x: x * 3, r_b=lambda y : y + 4):
    '''
    Функция, создающая бинарное дерево
    height: высота дерева
    root: значение корневого узла
    l_b: функция для вычисления левого потомка
    r_b: функция для вычисления правого потомка
    '''

    if height <= 0:
        return None
    if height == 1:
        return {str(root): []}
    ''' Возвращает None если высота дерева 0 и корень если высота дерева 1'''

    root_base = {'value': root, 'left': None, 'right': None}

    queue = collections.deque()
    '''Создание очереди для обхода уровня'''
    queue.append((root_base, 1))
    '''Добавление корневого узла и начального уровня'''

    while queue:
        current_root, level = queue.popleft()
        '''popleft() извлекает и удаляет первый элемент из очереди'''
        if level < height:
            '''
                Обработка левой ветки
            '''
            left_base = l_b(current_root["value"]) # Вычисление значения для левой ветки
            left_root = {"value": left_base} # Создание узла для левой ветки
            current_root["left"] = left_root # Присвоение левой ветки текущего узла
            queue.append([left_root, level + 1]) # Добавление левой ветки в очередь с увеличением уровня

            '''
              Обработка правой ветки
            '''
            right_base = r_b(current_root["value"]) # Вычисление значения для правой ветки
            right_root = {"value": right_base} # Создание узла для правой ветки
            current_root["right"] = right_root # Присвоение правой ветки текущего узла
            queue.append([right_root, level + 1]) # Добавление правой ветки в очередь с увеличением уровня

    return root_base
    ''' Возвращает дерево в виде словаря'''

def main():
    tree = gen_bin_tree()
    print('ваше дерево: : ', tree)

if __name__ == '__main__':
    main()