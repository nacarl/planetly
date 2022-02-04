# planetly task
The task took me about 4-5 hours to complete. I didn't work
with DRF before, but I thought it was a good opportunity to 
do so. The biggest trouble I had doing this was the docker
compose file, because the postgres server needs some time
to get running.

This project is my implemantation for a planetly coding challenge.
It is implemented with django and the django-restframework.
The proejct contains a docker-compose file to run the 
web server and data base server (postgres here).
This project is running the django development server which
should not be used in a production environment, but it 
serves the purpose of this task.

###run the application with docker-compose:
`cd planetly`

`docker-compose build`

`docker-compose up`

####The API should be running on localhost:8000/
The API contains the following endpoints:
* /usages
* /users
* /usage-types

CRUD operations are enabled for all endpoints
The API is protected with Token Authentication. You can authenticate 
on `127.0.0.1:8000/api-token-auth/` with a tool like postman to
get a token and use it with a browser extension like Chrome Modheader
to add the token to your requests headers:
`Authorization: Token <your_token>`
###Filtering:
A Date range filter can be applied for the usage: usage_at attribute like this:

`/usages/?usage_at_start=2019-01-01&usage_at_end=2021-01-01`

###Sorting:
Sorting is possible for following attribute:
* usage types: 'name', 'unit', 'factor'
* usages: 'usage_type'

e.g.: `/usages/?ordering=-usage_type`

###Pagination
Pagination is enabled and set to a page size of 5 for demonstration purposes.