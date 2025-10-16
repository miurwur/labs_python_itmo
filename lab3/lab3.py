def left_branch(root: int) -> int:
    '''Левый потомок'''
    return root * 3

def right_branch(root: int) -> int:
    ''' Правый потомок '''
    return root + 4

def gen_bin_tree(height = 2, root = 6, l_b=left_branch, r_b=right_branch):
    '''
    Функция, создающая бинарное дерево
    height: высота дерева
    root: значение корневого узла
    l_b: функция для вычисления левого потомка (по умолчанию left_branch)
    r_b: функция для вычисления правого потомка (по умолчанию right_branch)
    '''

    if type(height) != int:
        return "Введите целое число для высоты"
    if type(root) != int and type(root) != float :
        return "Введите числовое значение для корня"
    '''' Возвращает запрос ввести правильный тип данных для высоты или корня'''

    if height <= 0:
        return None
    if height == 1:
        return {str(root): []}

    ''' Возвращает None если высота дерева 0 и корень если высота дерева 1'''

    left_tree = gen_bin_tree(height - 1, l_b(root), l_b, r_b) if height > 1 else []
    right_tree = gen_bin_tree(height - 1, r_b(root), l_b, r_b) if height > 1 else []

    return {str(root): [left_tree, right_tree]}
    ''' Возвращает дерево в виде словаря'''

def main():
    tree = gen_bin_tree()
    print('ваше дерево: : ', tree)

if __name__ == '__main__':
    main()
