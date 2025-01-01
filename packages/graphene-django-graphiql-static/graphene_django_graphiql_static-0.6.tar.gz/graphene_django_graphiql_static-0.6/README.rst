===============================
graphene-django-graphiql-static
===============================

Graphene-Django-GraphiQL-Static provides an offline-compatible GraphiQL web UI for Graphene-Django projects. It ensures uninterrupted GraphQL query exploration by serving all necessary assets locally, making it reliable even during internet outages.

Documentation
-------------

The full documentation is at https://graphene-django-graphiql-static.readthedocs.io.

Quickstart
----------

Install graphene-django-graphiql-static::

    pip install graphene-django-graphiql-static

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        # Other installed apps
        'graphene_django_graphiql_static.apps.GrapheneDjangoGraphiqlStaticConfig',
    )

Add graphene-django-graphiql-static's URL patterns:

.. code-block:: python

    from graphene_django_graphiql_static import urls as graphene_django_graphiql_static_urls


    urlpatterns = [
        # Other installed apps
        url(r'^', include(graphene_django_graphiql_static_urls)),
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l

