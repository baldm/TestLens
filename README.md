# TestLens
A self-hosted backend to store test data, created as a simple demo of a Django REST API running in docker. TestLens is a very simple alternative to Xray Test Management, to store your results for any kind of project.

## How it works
Clone the repo and start it up with docker compose:
`docker-compose up -d`

TestLens uses both Swagger and Redoc to automatically document the API. Access it via:
http://your-ip:8000/swagger/ 
or
http://your-ip:8000/redoc/

The data structure can be simplified into this model:

![Model Structure](https://github.com/baldm/TestLens/blob/main/docs/database.drawio.png?raw=true)

### Projects
Projects are for your products. For this example e.g. your new mobile application.

### Test Sets
Test sets are collection of testcases, typically seperated into major features of your product. By seperating your testcases into sets you can easily identify which features are failing.

### Test Cases
Test cases are linked to only one test set. However it can have many test executions linked to it. 

### Environment
Environments are for simply tagging your test executions, to compare your results across e.g. operating systems.

# TODO
- [ ] Configure a production and debug environment with Docker
- [ ] Manage Django security and secrets
- [ ] Configure logging
- [ ] Endpoints for frontend dashboard
- [ ] Simple frontend dashboard for visualising test data
- [ ] Integrate Celery and Redis into backend