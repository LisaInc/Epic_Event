# Epic Event

Application faite avec Django Rest Framework

Documentation des endpoints de l'api faite avec postman à cette [adresse](https://documenter.getpostman.com/view/19707856/2s7YfSbXot)

Logs sur sentry.io

## Installation

```
git clone https://github.com/LisaInc/Epic_Event.git
```

Il est conseillé d'utiliser un environement virtuel.

```
python3 -m venv .venv
. .venv/bin/activate
```

Installation des librairies necessaires:

```
pip install -r requirements.txt
```

Pour executer le site

```
python manage.py runserver
```

Une fois exécuté, depuis un navigateur le site sera à l'adresse

* `http://localhost:8000 `pour les utilisateurs et
* `http://localhost:8000/admin` pour les managers
