# TestDrive Repo

This repo holds a super small django project to test basically several containers created with a `Dockerfile` 
and a `docker-compose.yml` :

	1. web -- django
	2. db -- postgres
	3. celery -- maps to a celery worker
	4. rabbitmq -- the rabbitmq broker
	5. redis -- redis useed a celery backend result holder
	6. Flower -- To check celery execution
	

## Dockerfile

This inherits from ubuntu, creates a directory, install the new reqs, and then stops.

## docker-compose.yml

This manage all the containers specification. Notable: the celery, flower and web container
are all using the same image to launch the file.

More about this in a blog post coming up @ http://blog.michelemattioni.me
