### Проект по автоматизации UI-тестов для сервиса «Яндекс. Самокат»

https://qa-scooter.praktikum-services.ru/

**Спринт 6, Page Object Model**

Описание тестов:
test_logo_redirect.py - тесты перехода на главную страницу сервиса и на главную страницу «Дзена»
test_main_page.py - тесты раздела Вопросы о важном
test_order_page.py - тесты заказа самоката


Вспомогательные файлы:
data.py - статические данные тестов
page_object.py - описание моделей страниц
conftest.py - фикстуры
locators.py - локаторы, используемые в тестах
requirements.txt - все внешние зависимости исполняемых тестов для удобной установки одной командой
README.md - описание проекта
.gitignore - список игнорируемых файлов в Git


Запуск всех тестов:
Команда для терминала: pytest -v

Установка зависимостей: 
pip install -r requirements.txt.

Отчет о тестировании:
Allure_results - allure-отчеты в формате веб-страницы генерируется командой allure serve allure_results.