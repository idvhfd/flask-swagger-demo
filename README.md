# flask-swagger-demo
Trying out flask-swagger with flask-RESTplus, simple project to get a doc spec going.

Inspired by: https://github.com/postrational/rest_api_demo

Concept/resources inspired by: https://github.com/pallets/flask/tree/master/examples/tutorial/

RestPlus resources used: https://flask-restplus.readthedocs.io/en/stable/quickstart.html 

## How to run?
Boot up `app.py` in any desired way, then simply navigate to the http://localhost:8888/api to see the Swagger doc in action.

In order to change the root URL, check out the `settings.py` file.

## I am getting 500 errors when trying to perform operations with the API!
This sounds like your DB file is not working. I ship a very simple version of a DB with a few basic students to make it easy to get going with it, but if yours is somewhy missing or corrupt, do the following:
* Delete your .sqlite file if any exists.
* Navigate to your `restplus_demo\database\__init__.py` and run the `reset_database` function to create a new sqlite DB file.

That's it! It should all work from here!
