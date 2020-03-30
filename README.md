# Platzigram

This is my implementation of [Platzi's Django Course](https://platzi.com/clases/django/).

## How is my implementation different to the one of the course?

* I removed the Middleware to require the user to add a Picture and a Website.

* I'm not importing the User directly from `django.contrib.auth.models` but rather using the `get_user_model` method to get the User instance, [as stated in the documentation](https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#django.contrib.auth.get_user_model).

* I'm creating the `Profile` for every user automatically by using a signal that listens to post_save of the `User` instance.

## What I'm missing?

* Implementation of the follow behavior.

* Implementation of the likes behavior.

## How to install the project's dependencies?

* Clone the repository:

```bash
git clone git@github.com:d4vsanchez/platzigram.git && cd platzigram
```

* Create a Python virtual environment:

```bash
python3 -m venv .env
```

* Activate the virtual environment:

```bash
source .env/bin/activate
```

* Install the requirements from the `requirements.pip` file:

```bash
pip install -r requirements.pip
```