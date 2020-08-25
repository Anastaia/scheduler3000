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
