from lab5 import gen_bin_tree
import unittest

class TestBinaryTree(unittest.TestCase):

    def test_height_two(self):
        ''' Тест 1: Стандартный вывод дерева высотой больше 1'''
        self.assertEqual(gen_bin_tree(2, 6), {'left': {'value': 18}, 'right': {'value': 10}, 'value': 6})
        self.assertEqual(gen_bin_tree(3, 6), {'value': 6, 'left': {'value': 18, 'left': {'value': 54}, 'right': {'value': 22}},
                                              'right': {'value': 10, 'left': {'value': 30}, 'right': {'value': 14}}}
)

    def test_height_zero(self):
        ''' Тест 2: При высоте равной 0 возвращает None'''
        self.assertEqual(gen_bin_tree(0, 4), None)

    def test_height_one(self):
        ''' Тест 3: При высоте равной 1 возвращает только корень'''
        self.assertEqual(gen_bin_tree(1, 4), {'4': []})
