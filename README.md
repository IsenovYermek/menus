### Виртуальное окружение и зависимости
```
python3 -m venv env
```
```
source env/bin/activate
```
Перейти в папку проекта и установить зависимости:
```
pip install -r requirements.txt
```
### Создать суперпользователя в Django
```
python manage.py createsuperuser
```

### Запустить проект
```
python manage.py runserver
```
### Добавить в ссылке /admin/, чтобы выглядело так http://127.0.0.1:8000/admin/ авторизоваться перейти во вкладку navigation
### нажать add и заполните форму в соответствии с примером ниже:
```
Title: Home
URL: /
Menu: main
Parent: (leave blank)

Title: About
URL: /about/
Menu: main
Parent: (leave blank)

Title: News
URL: /news/
Menu: main
Parent: (leave blank)

Title: Sports
URL: /news/sports/
Menu: main
Parent: News

Title: Politics
URL: /news/politics/
Menu: main
Parent: News
```
