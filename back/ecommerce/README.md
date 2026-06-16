### Django rest framework tutorial

## Config

**Using uv for Python**

```shell
cd /ruta/de/tu-proyecto
```

**1) Backup dependencies**

```shell
uv pip freeze > requirements.txt
```

**2) Create pyproject.toml minimum project exist**

```shell
uv init --bare
```

**3) Import dependencies format .toml**

```shell
uv add -r requirements.txt
```

**4) Option: pin python version**

```shell
uv python pin 3.14
```

**5) Rebuild venv clean way**

```shell
rm -rf .venv
```

```shell
uv sync
```

**6) Checks issues**

```shell
uv run python manage.py check
```

```shell
uv run python manage.py runserver
```

## New apps

**Create a django app**

```shell
cd apps/
```

```shell
uv run python manage.py startapp 'app_name'
```

**Rename app**

```text
app_name.apps.py and add prefix root folder, in this case is apps = apps.app_name
Example:
project:
    apps:
        users:
            app.py
                name = 'apps.users'
```

**Adds to main project**

```text
 INSTALLED_APPS=['apps.users'] in project.settings.py or project.settings.base.py: LOCAL_APPS = []

```

## New models

**Make migrations**

```shell
uv run python manage.py makemigrations
```

**Apply migrations**

```shell
uv run python manage.py migrate
```
