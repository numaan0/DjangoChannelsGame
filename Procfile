web: daphne tic_tac_toe.routing:application --port $PORT --bind 0.0.0.0 -v2
web2: gunicorn tic_tac_toe.wsgi
worker: python manage.py runworker channel_layer -v2