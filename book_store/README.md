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

```bash
poetry run python manage.py makemigrations
```

5. Apply migrations

```bash
poetry run python manage.py migrate
```