release: python manage.py migrate
gunicorn tic_tac_toe.asgi:application -w 4 -k uvicorn.workers.UvicornWorker
web: daphne tic_tac_toe.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A tic_tac_toe.celery worker -l info
celerybeat: celery -A tic_tac_toe beat -l INFO 
celeryworker2: celery -A tic_tac_toe.celery worker & celery -A tic_tac_toe beat -l INFO & wait -n
