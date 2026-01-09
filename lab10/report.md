**Отчет по лабораторной работе №10**  
Студент: Барыкина Анна  
Группа: P3122  

### Лабораторная работа 10. Методы оптимизации вычисления кода с помощью потоков, процессов, Cython, отпускания GIL  
## Цель работы  
Исследовать методы оптимизации вычисления кода, используя потоки, процессы, Cython и отключение GIL на основе сравнения времени вычисления функции численного интегрирования методом прямоугольников, реализованной на чистом Python.  

## Итерация 1: Базовая реализация:  
```python
def integrate(f: Callable[[float], float], a: float, b: float, *, n_iter: int = 100000) -> float:
```
Производительность:  
<img width="410" height="169" alt="image" src="https://github.com/user-attachments/assets/6ebc936a-bd47-4d4f-9a4b-116954bbb814" />

## Итерации 2 и 3: Оптимизация с помощью потоков и процессов 
```python
def integrate(f: Callable[[float], float], a: float, b: float, *, n_iter: int = 100000) -> float:
...
def integrate_async(
    executor_cls: Union[Type[ftres.ThreadPoolExecutor], Type[ftres.ProcessPoolExecutor]],
    func: Callable[[float], float],
    a: float,
    b: float,
    *,
    n_jobs: int = 2,
    n_iter: int = 1000000
) -> float:
```

Производительность:  
<img width="444" height="266" alt="image" src="https://github.com/user-attachments/assets/1930ba6b-9474-465b-a6b5-759427990ae0" />

## Итерация 4: Оптимизация с помощью Cython  
```python
%%cython -a
# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False
# cython: cdivision=True

def integrate_cy(double a, double b, int n_iter):
    """
    Оптимизированная функция на Cython
    использует чистые типы C и математическую библиотеку C (libc)
    """
    cdef double acc = 0.0
    cdef double step = (b - a) / n_iter
    cdef int i

    # Цикл превращается в C код без участия объектов Python
    for i in range(n_iter):
        acc += sin(a + i * step) * step

    return acc
...

# Итерации 2 и 3 с использованием Cython
def run_parallel(executor_class, n_jobs, n_iter):
    step_total = math.pi / n_jobs  # длина каждого подынтервала
    iter_per_job = n_iter // n_jobs  # итераций на каждый worker
...
```


Производительность:  
<img width="724" height="249" alt="image" src="https://github.com/user-attachments/assets/6ff0ea5b-99e7-43e7-a0b1-a38c0d522a9c" />

## Итерация 5: Cython с NOGIL  
```python

def integrate_nogil(double a, double b, int n_iter):
    cdef double acc = 0.0
    cdef double step = (b - a) / n_iter
    cdef int i

    # Отпускаем GIL, благодаря чему другие потоки могут выполняться параллельно с циклом
    with nogil:
        for i in range(n_iter):
          acc += sin(a + i * step) * step

    return acc
```

Производительность:   
<img width="550" height="194" alt="image" src="https://github.com/user-attachments/assets/063027b6-8493-4d62-963e-222931a6751c" />

