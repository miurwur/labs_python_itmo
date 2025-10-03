from lab2 import guess_number
import unittest

class TestFunctions(unittest.TestCase):

    def test_bin(self):
        self.assertEqual(guess_number(6, [1, 2, 3, 4, 5, 6, 7, 8, 9], type = "bin"),
                         ['Ваше число: ', 6, 'Количество сравнений: ', 2])
        self.assertEqual(guess_number(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], type="bin"),
                         ['Ваше число: ', 5, 'Количество сравнений: ', 0])

    def test_seq(self):
        self.assertEqual(guess_number(6, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
                         ['Ваше число: ', 6, 'Количество сравнений: ', 5])
        self.assertEqual(guess_number(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                         ['Ваше число: ', 5, 'Количество сравнений: ', 4])

    def test_no_elem(self):
        self.assertEqual(guess_number(1, [2, 3, 4, 5, 6, 7, 8, 9, 10]),
                         [None, 'Количество сравнений: ', 9])
        self.assertEqual(guess_number(1, [2, 3, 4, 5, 6, 7, 8, 9, 10], type="bin"),
                         [None, 'Количество сравнений: ', 3])

    # def test_diap(self):
    #     self.assertEqual(guess_number(1, 5), [1, 2, 3, 4, 5])
    #     self.assertEqual(guess_number(5, 1), [1, 2, 3, 4, 5])
    #     self.assertEqual(guess_number(-2, 2), [-2, -1, 0, 1, 2])
    #     self.assertEqual(guess_number(3, 3), [3])
    #     self.assertEqual(guess_number(10, 15), [10, 11, 12, 13, 14, 15])
    #
    # def test_guess_number_seq(self):
    #     lst = list(range(10))
    #     # Тест существующего элемента
    #     self.assertEqual(guess_number(5, lst), [5, 5])
    #     # Тест несуществующего элемента
    #     self.assertEqual(guess_number(20, lst), [None, 10])
    #
    # def test_guess_number_bin(self):
    #     lst = list(range(10))
    #     # Тест существующего элемента
    #     self.assertEqual(guess_number(7, lst, type='bin'), [7, 1])
    #     # Тест несуществующего элемента
    #     self.assertEqual(guess_number(20, lst, type='bin'), [None, 3])

if __name__ == '__main__':
    unittest.main()