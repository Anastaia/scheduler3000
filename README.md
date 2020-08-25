#**Scheduler 3000**

Используемые фреймворки:
-  Bootstrap
-  Flask

Необходимые библиотеки находятся в requriments.txt

Запуск:
1. Склонировать репозиторий себе
2. Установить зависимости "python -m pip install -r requriments.txt"
3. Запуск "python run.py"


Создание БД:
1. Python Shell
2. from Scheduler3K import db
3. from Scheduler3K.models import User, Group
4. db.create_all()


Scheduler3K - пакет со всеми модулями.
run.py - исполняемый файл
В пакете Scheduler3K находятся:
- routes.py
  Отвечает за обработку всех ссылок.
- models.py
  Отвечает за репрезентацию сущностей базы данных в коде питона
- forms.py
  Отвечает за обработку форм, на основе которых генерируется html-формы для пользователей
- \__init__.py
  Отвечает за настройку фреймворка

Шаблоны
- layout.html
  Основной шаблон, который расширяют другие, с нужным содержимым
- home.html
  Главная страница
- account.html
  Страница, на которой можно изменить группу или добавить расписание для группы
- login.html
  Страница входа в систему
- register.html
  Страница регистрации
- timetable.html
  Страница с выбранным расписанием
