# Автотесты для сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/)

Сервис [Stellar Burgers](https://stellarburgers.nomoreparties.site/) - это космический фастфуд: можно собрать и заказать 
бургер из необычных ингредиентов.

Это учебное приложение: его написал студент Практикума на курсе «React-разработчик».

## Структура проекта 

* [tests](tests) - директория с тестами
* [tests/conftest.py](tests/conftest.py) - файл с проверками переходов к разделам «Булки»,
«Соусы», «Начинки»
* [tests/conftest.py](tests/logout_from_account_test.py) - файл с проверками выхода из личного кабинета
* [tests/conftest.py](tests/sign_in_page_tests.py) - файл с проверками авторизации
* [tests/conftest.py](tests/sign_up_page_tests.py) - файл с проверками регистрации
* [tests/conftest.py](tests/transition_from_personal_account_tests.py) - файл с проверками перехода из личного кабинета
* [tests/conftest.py](tests/transition_to_personal_account_tests.py) - файл с проверками перехода в личный кабинет
* [data.py](data.py) - файл с данными для регистрации и входа
* [locators.py](locators.py) - файл с локаторами элементов
* [urls.py](urls.py) - файл с урлами страниц

## Запуск тестов

Для запуска тестов выполнить:
```bash
pytest
```
