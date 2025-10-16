from bin_rec import build_tree_recursive, left_branch, right_branch
from bin_non_rec import build_tree_iterative

import timeit
import matplotlib.pyplot as plt
import random


def benchmark(func, n, repeat=5): # это дописать, верхнюю делитнуть
    """Возвращает среднее время выполнения func(n)"""
    times = timeit.repeat(lambda: func(n), number=1, repeat=repeat)
    return min(times)

def main():
    # фиксированный набор данных
    random.seed(2)
    test_data = list(range(2, 20, 2))

    res_recursive = []
    res_iterative = []

    for n in test_data:
      res_recursive.append(benchmark(build_tree_recursive,n))
      res_iterative.append(benchmark(build_tree_iterative,n))

    # Визуализация
    plt.plot(test_data, res_recursive, label="Рекурсивный")
    plt.plot(test_data, res_iterative, label="Итеративный")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение рекурсивного и итеративного дерева")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()