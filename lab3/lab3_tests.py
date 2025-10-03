from lab3 import gen_bin_tree
import unittest

class TestBinaryTree(unittest.TestCase):

    def test_height_two(self):
        ''' Тест 1: Стандартный вывод дерева высотой больше 1'''
        self.assertEqual(gen_bin_tree(2, 6), {'6': [{'18': []}, {'10': []}]})
        self.assertEqual(gen_bin_tree(3, 6), {'6': [{'18': [{'54': []}, {'22': []}]}, {'10': [{'30': []}, {'14': []}]}]})

    def test_height_zero(self):
        ''' Тест 2: При высоте равной 0 возвращает None'''
        self.assertEqual(gen_bin_tree(0, 4), None)

    def test_height_one(self):
        ''' Тест 3: При высоте равной 1 возвращает только корень'''
        self.assertEqual(gen_bin_tree(1, 4), {'4': []})

    def test_height_type(self):
        ''' Тест 4: Неправильный тип данных для высоты'''
        self.assertEqual(gen_bin_tree(2.5, 2.5), 'Введите целое число для высоты')

    def test_root_type(self):
        ''' Тест 5: Неправильный тип данных для корня'''
        self.assertEqual(gen_bin_tree(5, True), 'Введите числовое значение для корня')
