
def gen_bin_tree(height = 2, root = 6, l_b=lambda x: x * 3, r_b=lambda y : y + 4):
    '''
    Функция, создающая бинарное дерево
    height: высота дерева
    root: значение корневого узла
    l_b: функция для вычисления левого потомка
    r_b: функция для вычисления правого потомка
    '''

    if height == 0:
        return None
    if height == 1:
        return {str(root): []}
    ''' Возвращает None если высота дерева 0 и корень если высота дерева 1'''

    left_tree = gen_bin_tree(height - 1, l_b(root), l_b, r_b) if height > 1 else []
    right_tree = gen_bin_tree(height - 1, r_b(root), l_b, r_b) if height > 1 else []

    return {str(root): [left_tree, right_tree]}
    ''' Возвращает дерево в виде словаря'''