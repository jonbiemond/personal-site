Title: Django: quickstart
Date: 2026-11-26 08:04
Tags: Django
Slug: django-quickstart
Author: Jonathan Biemond
Summary: The basics of starting a new Django project.

Initialize a new Django project, starting from an empty directory with just the bare minimum steps and no fluff.

## Prerequisites
You must have these installed to begin.

* [Python installed](https://www.python.org/downloads/).
* [uv installed](https://docs.astral.sh/uv/getting-started/installation/).

Note: If this is your first Django project, begin with a tutorial instead.
The [official Django tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/) covers everything below and more in detail.

## Initialize Python Project
Starting from an empty directory for your new project, initialize the Python project.
```bash
uv init --no-package --app .
```

No need for the `main.py` file.
```bash
rm main.py
```

Install Django.
```bash
uv add django
```

## Initialize Django Project
Create the Django project files, using `project` as the folder name.
```bash
uv run django-admin startproject project .
```

Create a Django app called "core".
```bash
uv run manage.py startapp core
```

Add core to `INSTALLED_APPS` in `project/settings.py`.
```python
INSTALLED_APPS = [
    ...,
    "core",
]
```

Running the development server should now display the Django launch page at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
```bash
uv run manage.py runserver
```

## Create a View
Add a new view to `core/views.py`.
```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World!")
```

Route view to be the front page in `core/urls.py`.
```python
from django.urls import path

from core import views


urlpatterns = [
    path("", views.index, name="index"),
]
```

Include core url patterns in `project/urls.py`:
```python
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
]
```

With `runserver` still running, refresh [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see your new view.

## Next Steps
* Edit `pyproject.toml` with project name and description.
* Pick a database.
* Configure a [custom user](https://docs.djangoproject.com/en/dev/topics/auth/customizing/#substituting-a-custom-user-model).
* Run migrations.
* Add your favourite third-party Django packages.
* Install and configure linters and formatters.
* Add a `base.html` template.

## Getting Help
For help with starting your project visit the wonderful community in the [Django Forum](https://forum.djangoproject.com/) or the [Django Discord Server](https://discord.gg/django-856567261900832808) (I like to hang out here).
