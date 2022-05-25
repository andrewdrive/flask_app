# flask_app
Настройка
========

Добавляем зависимости в виртуальное окружение `venv`:


    $ python -m venv env
    $ source env/bin/activate
    $ cd flask_app/
    $ pip install -r requirements.txt

Настройка переменных окружения `env` находясь в директории flask_app/:


    $ export FLASK_APP=project
    $ export FLASK_DEBUG=0

(v1) Если нужна новая база sqlite:
В интерпретаторе пишем:


    >> from project import db, create_app, models
    >> db.create_all(app=create_app())


Запуск
======
По умолчанию на `127.0.0.1:5000`:


    $ flask run
