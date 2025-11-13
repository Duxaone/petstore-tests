# Petstore API Tests

Пример проекта автоматизированных тестов для публичного API [Swagger Petstore](https://petstore.swagger.io).

Тесты покрывают CRUD: POST, GET, PUT, DELETE.

Добавлен pytest.ini с настройками, requirements.txt с фиксированными версиями.

## Стек технологий
- Python 3.10+
- Pytest
- Requests
- Pytest-order (для последовательного запуска тестов)

## Как запустить проект локально

1. Клонировать репозиторий:
   
   ```bash
   git clone https://github.com/DuxaOne/petstore-tests.git
   cd petstore-tests
3. Установить зависимости:
   
   ```
   pip install -r requirements.txt
5. Запустить тесты:

   ```
   pytest -v
