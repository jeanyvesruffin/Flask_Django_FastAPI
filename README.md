# Flask_Django_FastAPI

TDD création d'un site web (MVC).

# Django (\Flask_Django_FastAPI\DJANGO)

## Prerequis et installation projet

* Installer `Python` et `Django`
* Vérifications:

```shell
python --version
#Python 3.14.4
python
>>> import django
>>> print(django.get_version())
#6.1.1
```

* Création environnement virtuel `.env`

```shell
python -m venv .env
```

* Puis `sourcer` l'environnement virtuel

```shell
source .env/Scripts/activate
#(.env)
```

* Vérification de la `version` python utilisée par le projet

```shell
which python
# /c/Users/ruffi/WORKSPACE/Flask_Django_FastAPI/.env/Scripts/python
```

* `Activation de Django` dans le projet

```shell
source .env/Scripts/activate
python.exe -m pip install --upgrade pip
pip install django==6.1.1
# Verification
#python -m django --version
#6.1.1
```

* Création du fichier de configuration `requirements.txt` pour figer les dependances

```shell
source .env/Scripts/activate
pip freeze > requirements.txt
# Verification
#python -m django --version
#6.1.1
```

* Dans le cas d'un premier démarrage, apres un clone, il suffit d'éxécuter les commandes suivantes afin de re-télécharger les dependances
  
```shell
python -m venv .env
source .env/Scripts/activate
pip install -r requirements.txt
```

* Pièges :
  * Toujours source votre projet `source .env/Scripts/activate`
  * La configuration python et django se trouve dans le fichier `activate`

## Création projet django (DocBlog)

```shell
#django-admin startproject <Project name>
django-admin startproject DocBlog
#help django
django-admin help
```

## Structure du projet django

```shell
$ tree
.
|-- DocBlog
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
```

* `manage.py` permet d'executer d'autre commandes python
* `DocBlog/urls.py` permet de définir les chemins des urls qui seront redirigés vers les vues.
* `DocBlog/settings.py` définie toutes les preferences de notre application (logger, template, database ...) équivalent applciation.properties en maven.

## Execution du serveur de développement (local hors production)

```shell
cd src
python manage.py migrate
python manage.py runserver
# http://127.0.0.1:8000
# Ctrl + C pour stopper le server
```

![Accueil Django](DJANGO/Docs/imgs/Django.png)

## Créer un chemin d'url pour afficher une vue dans notre projet

Exemple création d'une route retourrnant la vue pour une erreur 500

```shell
# fichier urls.py
from django.views.defaults import server_error

urlpatterns = [
    path('bonjour/', server_error),
]
# affiche a l'url http://127.0.0.1:8000/bonjour/
# Server Error (500)
```

## Le paramètre append_slash

Parmètrage de la variable d'environnement `append_slash`, intêret sur la résolution des chemins d'urls avec Django.
Cela permet de faire le routage sur des urls contenant ou non le `/` de fin par default à `True`.
Par default, si le `/` de fin de chemin d'url est absent alors lors de l'appel de la route, par exemple `/test` sera redirigé vers `/test/`, append_slash ajoute un `/` à la fin de la route mais génére deux requetes une sur `/test` puis redirection vers `/test/`.
Le passer à `False`, `APPEND_SLASH = False` dans `settings.py`, cela permettra de nous retourner une erreur 404 sans redirection sur l'url avec le `/` de fin.

## Création d'une vue pour une url donnée

* Création d'une vue `[index.view.py](DJANGO/src/DocBlog/index.view.py)`
* Ajout fonction qui nous retourne une  `HttpResponse from django.http import HttpResponse`

```py
# index.view.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Bonjour, bienvenue sur mn site</h1>")
# urls.py
from .index.view import index
urlpatterns = [
    path('', index, name="index"),
]
```

## Création de templates html

* Créer un dossier `templates`, (DJANGO\src\DocBlog\templates)
* Ajouter votre dossier template dans vos settings `settings.py`
* Ajouter un fichier `index.html` au dossier `templates`
* Ajouter le contenu du fichier `index.html`
* ré-écrire votre fonction index de `index.view.py`
  
```py
# settings.py
TEMPLATES = [
    {
        'DIRS': [
            os.path.join(BASE_DIR, "DocBlog/templates")
        ],
    },
]
# index.view.py
from django.shortcuts import render
def index(request):
    return render(request, "index.html")

```

## Insérer des données dans un template

1. Cas de données hard code:
   1. ajouter `context={clé: valeur}`, pour definir un catalogue de données dans `index.view.py`.
   2. dans `index.html`, récupérer la donnée à l'aide des `{{}}`.
   3. possibilité d'ajouter un `|` pour faire un traitement sur le resultat (équivalent pipe Angular)

```py
# index.view.py
from django.shortcuts import render
def index(request):
    return render(request, "index.html", context={"prenom": "Jean-Yves"})
# index.html
    <h1>Bonjour {{ prenom | upper}}, bienvenu sur mon site DJANGO</h1>
    <h2>Nous sommes le {{ date|date:"d F Y H:i:s"}}</h2>
```

* Ressources :
[Django template filter](https://docs.djangoproject.com/en/6.1/ref/templates/builtins/#built-in-filter-reference)
[Code language](http://www.i18nguy.com/unicode/language-identifiers.html)

