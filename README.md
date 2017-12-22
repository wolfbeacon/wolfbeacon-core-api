# WolfBeacon Core API

WolfBeacon's Core API for Mobile and Analytics.

Written in [Python 3](https://www.python.org/downloads/release/python-352/), powered by [Django](https://www.djangoproject.com/), [Django Rest Framework](http://www.django-rest-framework.org/), [PostgreSQL](https://www.postgresql.org/).

## API Usage and Documentation

#### API Documentation is available at [https://api.wolfbeacon.com/docs](https://api.wolfbeacon.com/docs)

Documentation is to be used in conjunction with the [WolfBeacon Core API Integration Guide](https://wolfbeacon.atlassian.net/wiki/spaces/WG/pages/283181225/WolfBeacon+API+Integration) which describes various crucial flows like Login, Signup etc.

**Note**: Docs are generated using [apidoc](http://apidocjs.com/) with corresponding docstrings present in view files under the `/api/views` directory. Documentation is served separately by the [wolfbeacon-apidoc-gen](https://github.com/wolfbeacon/wolfbeacon-apidoc-gen) service.

## Local Development Setup

* [Install virtualenv supporting Python 3.5](https://stackoverflow.com/questions/29934032/virtualenv-python-3-ubuntu-14-04-64-bit) and activate it

  `virtualenv venv && source venv/bin/activate`
* Make a *settings.py* file from the *settings.template.py* file provided

  `cp wolfbeacon/settings.template.py wolfbeacon/settings.py`

* Add the *SECRET_KEY*, *DATABASES* and *AUTH0* configuration in the *settings.py* file.

  Adding the *AUTH0* configuration (used for [Auth0](https://auth0.com) Token Validation) is optional. Hence for local testing, disable it by removing `'api.middleware.auth0.Auth0Middleware',` from *MIDDLEWARE*.

* Install requirements

  `sudo pip install -r requirements.txt`

* Run database migrations

  `python manage.py migrate`

* Start development server

  `python manage.py runserver`


## Running in Production with Docker

Make sure [Docker](https://docs.docker.com/engine/installation/) is installed on your system. We run this API a Dockerized application in production.

Assuming Postgres is already running in a separate container remotely accessible and the *settings.py* file is all configured, we are ready to go. Simply build a docker image for this application and run it.

* `sudo docker build -t wolfbeacon-core-api .`
* `sudo docker run -p 8000:8000 wolfbeacon-core-api`

This should have have your app up and running, accessible on port 8000.

## AWS CodeDeploy Env Variables

`CORE_S3_CONFIG_PATH` - wolfbeacon/settings.py S3 path

## Simulating Production Environment Locally

For local testing purposes, a production environment can be simulated using the provided docker-compose file. It bundles the API and Postgres together. Currently, migrations are manually run after both the containers start.

* `cp wolfbeacon/settings.docker-compose.py wolfbeacon/settings.py`

* Comment out line 38 from the Dockerfile which makes DB Migrations

  `# RUN /venv/bin/python manage.py migrate`

* `sudo docker-compose up --build -d`

* `sudo docker exec -it <wolfbeaconapi_container_id> sh`

* `/venv/bin/python manage.py migrate`
