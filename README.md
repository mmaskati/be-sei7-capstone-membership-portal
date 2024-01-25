# Membership Portal Backend

Backend server for membership portal app, the server is has both REST API and a client.

The REST API is responsible for user operations and all required endpoints and API routes to power the client applications.

The client app is a portal that can be used by application owner to perform admin tasks.

## Entity Relationsjip Diagram

https://drive.google.com/file/d/11NFxucsY-oLUPudnvShq-uWaoXBVbixX/view

## Trello User Stories

https://trello.com/invite/b/gMzU5mQU/ATTI8a084a091f817702c660eb86838a36660F10FBC1/membership-portal

## Technology Stack

The backend is powered by Python, django, PostgreSQL

## Dependencies

Python packages are required to run the server, run `pip install` with the following packages:

PIP install pakacges: 
```
pip install django_rest_framework djangorestframework_simplejwt django-cors-headers django-bootstrap4 django-bootstrap-datepicker-plus
```

Create `.env` file in root directory and add the following required enivromental variables

```
DATABASEHOSTNAME = PostgreSQL address
DATABASENAME = 
DATABASEUSER = 
DATABASEPASSWORD = 
DATABASEPORT = 5432
```

## Features

* Backend user authentication and access token.
* Backend input verification for most of the API endpoints.
* CRUD operations for users, profiles, benefits and events.
* Admin portal interface to perform superuser actions.

## API Documentation
Most REST API endpoints are documented using postman, click [here to view the docs](https://documenter.getpostman.com/view/16097405/2s9YynnQFx#bba516ef-8787-4f22-8e05-6c488f05f330)

## Future Plans

* Role authentication and restrictions.
* Invoice and payment routes.
* Search feature.
