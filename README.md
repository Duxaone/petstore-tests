Petstore API Tests

Пример проекта автоматизированных тестов для публичного API [Swagger Petstore](https://petstore.swagger.io).

  Стек технологий
- Python 3.10+
- Pytest
- Requests
- Pytest-order (для последовательного запуска тестов)

  Тесты покрывают CRUD: POST, GET, PUT, DELETE.
  Добавлен pytest.ini с настройками, requirements.txt с фиксированными версиями.

Как запустить проект локально:

1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/<твоя_ссылка>/petstore-tests.git
   cd petstore-tests

2. Установить зависимости:

   pip install -r requirements.txt

3. Запустить тесты:

   pytest -v
