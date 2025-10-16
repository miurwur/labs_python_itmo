from bin_rec import build_tree_recursive, left_branch, right_branch
from bin_non_rec import build_tree_iterative

import timeit
#import matplotlib.pyplot as plt
import random

def tree_recursive(build_tree_recursive, height, number=1, repeat=5):
    """Возвращает среднее время выполнения func на наборе data"""
    total = 0
    # for n in height:
    # несколько повторов для усреднения
    times = timeit.repeat(lambda: build_tree_recursive(height=height), number=number, repeat=repeat)
    return min(times)
    #     total += min(times)  # берём минимальное время из серии
    # return total / len(height)


def benchmark(func, height, repeat=5): # это дописать, верхнюю делитнуть
    """Возвращает среднее время выполнения func(n)"""
    # times = timeit.repeat(lambda: func(n), number=1, repeat=repeat)
    times = timeit.repeat(lambda: build_tree_recursive(height=height), repeat=repeat)
    return min(times)

def main():
    # фиксированный набор данных
    random.seed(42)
    test_data = list(range(10, 300, 10))

    res_recursive = []
    res_iterative = []

    for n in test_data:
      res_recursive.append(benchmark(build_tree_recursive,n))
      res_iterative.append(benchmark(build_tree_iterative,n))

if __name__ == "__main__":
    main()
