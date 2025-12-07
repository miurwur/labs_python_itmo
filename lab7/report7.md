**Цели работы**  
Освоить принципы разработки декораторов с параметрами  
Научиться разделять ответственность функций (бизнес-логика) и декораторов (сквозная логика)  
Научиться обрабатывать исключения, возникающие при работе с внешними API  
Освоить логирование в разные типы потоков (sys.stdout, io.StringIO, logging)  
Научиться тестировать функцию и поведение логирования  

**Реализация декоратора logger**  
Исходный код декоратора с параметрами: https://github.com/miurwur/labs_python_itmo/blob/main/lab7/logger.py  

Декоратор `logger` является параметризуемым с сигнатурой:
```python
def logger(func=None, *, handle=sys.stdout):
```  
Декоратор поддерживает три варианта логирования:
Вариант 1: Обычный поток вывода (по умолчанию)
```python
@logger
def example_function(x):
    pass
    ...
```
Вариант 1: Объект с файловым интерфейсом
```python
import io
stream = io.StringIO()

@logger(handle=stream)
def example_function():
    pass
```
3. Вариант 3: Объект модуля logging
```python
import logging
log = logging.getLogger("MyLogger")

@logger(handle=log)
def example_function():
    return "result"
```  
**Обязанности декоратора**  
1)Логирование старта вызова  
Уровень: INFO  
2)Логирование успешного завершения  
Уровень: INFO  
3)Логирование исключений  
Уровень: ERROR  

**2. Реализация функции get_currencies**
Исходный код get_currencies (без логирования): https://github.com/miurwur/labs_python_itmo/blob/main/lab7/currencies.py  

Функция `get_currencies` содержит только бизнес-логику без логирования:

```python
@logger
def get_currencies(currency_codes: list, url: str = "https://www.cbr-xml-daily.ru/daily_json.js") -> dict:
```

**Что делает функция:**  
1)Выполняет запрос к публичному API Центрального банка России для получения актуальных курсов валют
2)Извлекает словарь `Valute`  
3)Возвращает словарь вида `{"USD": 93.25, "EUR": 101.7}`  

**Когда выбрасывает исключения:**  
1)`ConnectionError` - если API недоступен  
2)`ValueError` - если некорректный JSON  
3)`KeyError` - если нет ключа "Valute" или валюта отсутствует  
4)`TypeError` - если курс валюты имеет неверный тип  

## Демонстрационный пример (квадратное уравнение).
Реализована функция `solve_quadratic` с декоратором quad_logger.
```python
quad_logger = logging.getLogger("QuadraticSolver")
quad_logger.setLevel(logging.INFO)

@logger(handle=quad_logger)
def solve_quadratic(a, b, c):
```

## Файловое логирование

Реализована функция logging.getLogger() для настройки логгера с записью в файл:

```python
file_logger = logging.getLogger("currency_file")
file_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("currencies.log", mode='a', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
```

Логи записываются в файл `currencies.log`: https://github.com/miurwur/labs_python_itmo/blob/main/lab7/currencies.log  
```
2025-12-06 16:42:33,851 - currency_file - INFO - INFO: Started 'get_currencies'. args: (['USD', 'EUR'],), kwargs: {}
2025-12-06 16:42:34,103 - currency_file - INFO - Finished 'get_currencies'. Result: {'USD': 76.0937, 'EUR': 88.7028}
```
## Тестирование  
Файл с тестами: https://github.com/miurwur/labs_python_itmo/blob/main/lab7/tests.py  
  
Тестирование функции get_currencies  
Используется модуль unittest с мокированием сетевых запросов:  
test_get_currencies_success - Проверка корректного возврата курсов валют  
test_get_currencies_connection_error - Проверка выброса ConnectionError при ошибках сети  
test_get_currencies_http_error - Проверка выброса ConnectionError при HTTP-ошибках  
test_get_currencies_invalid_json - Проверка выброса ValueError при некорректном JSON  
test_get_currencies_missing_valute_key - Проверка выброса KeyError при отсутствии ключа 'Valute'  
test_get_currencies_missing_currency_code - Проверка выброса KeyError при несуществующей валюте  
test_get_currencies_invalid_rate_type - Проверка выброса TypeError при нечисловом курсе валюты  
  
Тестирование декоратора logger  
Тесты покрывают различные варианты использования декоратора логирования:  
test_logging_success_info - Проверка логирования INFO при успешном выполнении функции  
test_logging_error_and_rethrow - Проверка логирования ERROR и проброса исключений  
test_logging_error_with_currency_context - Интеграционный тест с проверкой логирования ошибок сетевых запросов  
test_logger_with_logging_obj - Проверка работы с объектом logging.Logger вместо потока вывода  

