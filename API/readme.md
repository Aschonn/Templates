In python developement there are many different ways to create an API. Whether that is through flask rest api, django rest framework, fastapi, or create it from scratch. 

As the name suggests fastapi is very fast and will be used at my current job, so here's a framework to start with


Simple run commands for fastapi:

Run server: uvicorn {filename or directory}:app --reload



Interactive API documentation and shows responses
run redoc   -> `http://127.0.0.1:8000/docs.`

API schema generator
run openapi -> `http://127.0.0.1:8000/openapi.json.`