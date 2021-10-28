# web-testing-task
Automate testing with Selenium page objects + Pytest

Тест сценарий №1:
"""Неавторизованный пользователь
            заходит в https://www.google.com/
            ищет ivi
            переходит в картинки
            выбирает большие
            убеждается, что не менее 3 картинок в выдаче ведут на сайт ivi.ru"""
            
Тест сценарий №2:
"""Неавторизованный пользователь
            заходит в https://www.google.com/
            ищет ivi
            на первых 5 страницах находит ссылки на приложение ivi в play.google.com
            убеждается, что рейтинг приложения на кратком контенте страницы совпадает с рейтингом при переходе"""

Тест сценарий №3:
"""Неавторизованный пользователь
            заходит в https://www.google.com/
            ищет ivi
            на первых 5 страницах находит ссылку на статью в wikipedia об ivi
            убеждается, что в статье есть ссылка на официальный сайт ivi.ru"""
            
Отсутствие авторизации гарантировано уникальностью сессии и может быть подтверждено кукис с помощью библиотеки requests.
            
Использован принцип POM.
Фреймворк Pytest

запуск с системной переменной:
python -m pytest -v

с html отчетом:
python -m pytest -v --html=./result_name.html

синхронный запуск с поддержкой pytest: - требуется доработка(
python -m pytest xdist -n {i} #i - кол-во групп
