
install:
    python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

init_db
    python manage.py makemigrations

run-dev
    python manage.py runserver 0.0.0.0:8000

app
    python manage.py startapp ${app_name}