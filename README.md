# QA Practice Project

Проект для практики автоматизации тестирования на Python.

## Стек
- Python 3.14
- pytest
- requests

## Тесты
- `test_first.py` — базовые тесты на Python функции
- `test_api.py` — API тесты для jsonplaceholder.typicode.com

## Запуск тестов
```bash
pip install pytest requests
pytest -v
```

## Что покрыто
- Проверка статус кодов (200, 404)
- Проверка количества записей
- Проверка полей конкретного объекта
- Негативные тесты