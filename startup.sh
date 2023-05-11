export LANG=C.UTF-8

gunicorn --bind=0.0.0.0 --timeout 600 project.wsgi celery -A project worker -l INFO -B