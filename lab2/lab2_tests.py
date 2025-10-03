from lab2 import guess_number
import unittest

class TestFunctions(unittest.TestCase):

    def test_bin(self):
        ''' Тест 1: Бинарный поиск '''
        self.assertEqual(guess_number(6, [1, 2, 3, 4, 5, 6, 7, 8, 9], type = "bin"),
                         ['Ваше число: ', 6, 'Количество сравнений: ', 2])
        self.assertEqual(guess_number(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], type="bin"),
                         ['Ваше число: ', 5, 'Количество сравнений: ', 0])

    def test_seq(self):
        ''' Тест 2: Последовательный поиск '''
        self.assertEqual(guess_number(6, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
                         ['Ваше число: ', 6, 'Количество сравнений: ', 5])
        self.assertEqual(guess_number(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                         ['Ваше число: ', 5, 'Количество сравнений: ', 4])

    def test_no_elem(self):
        ''' Тест 3: Отсутствие элемента в списке '''
        self.assertEqual(guess_number(1, [2, 3, 4, 5, 6, 7, 8, 9, 10]),
                         [None, 'Количество сравнений: ', 9])
        self.assertEqual(guess_number(1, [2, 3, 4, 5, 6, 7, 8, 9, 10], type="bin"),
                         [None, 'Количество сравнений: ', 3])

    def test_lst(self):
        ''' Тест 4: Список длины = 1 без элемента '''
        self.assertEqual(guess_number(25, [1,1]),
                         [None, 'Количество сравнений: ', 2])
        self.assertEqual(guess_number(25, [1, 1], type="bin"),
                         [None, 'Количество сравнений: ', 2])
        ''' Тест 4: Список длины = 1, содержащий элемент '''
        self.assertEqual(guess_number(25, [25, 25]),
                         ['Ваше число: ', 25, 'Количество сравнений: ', 0])
        self.assertEqual(guess_number(25, [25,25], type="bin"),
                         ['Ваше число: ', 25, 'Количество сравнений: ', 0])