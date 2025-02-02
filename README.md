# Django Project

I am using poetry to manage the dependencies and the project.

to run the project:

```bash
poetry install
poetry run python manage.py runserver
```

to run the tests:

```bash
poetry run pytest
```

to apply migrations:

```bash
poetry run python manage.py migrate
```

## Purpose

This is a django project to learn the basics of django.
- [x] Create a new django project
- [x] Create a new app
- [x] Create a new model
- [x] Create a new view
- [x] Create a new url
   - learn how to use reverse to create dynamic urls
   - learn how to use HttpResponseRedirect to redirect to a new url
   - learn how to use HttpResponseNotFound to return a 404 error
   - learn how to use HttpResponse to return a response
   - learn about the routing system in django
- [x] Create templates
   - Created a base template that other templates inherit from
   - Created challenge.html template to display monthly challenges
   - Added header template as a reusable component
   - Used template filters like title to format text
   - Implemented template inheritance and includes
   - Added static files (CSS) to style the templates
