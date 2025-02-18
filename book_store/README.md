# Steps used to create the project

1. Create the project

```bash
poetry run python django-admin startproject book_store
```

2. Create the app

```bash
poetry run python manage.py startapp book_outlet
```

3. Run the server

```bash
poetry install
poetry run python manage.py runserver
```

4. Make migrations
- Every time we create, update or delete a model (database table schema), we need to make migrations

```bash
poetry run python manage.py makemigrations
```

5. Apply migrations
- Apply the migrations to the database every time we make migrations

```bash
poetry run python manage.py migrate
```

6. Python shell that I can use to interact with the database

```bash
poetry run python manage.py shell
```

7. Create a superuser

```bash
poetry run python manage.py createsuperuser
```


