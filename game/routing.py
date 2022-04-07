#from django.conf.urls import url
from game.consumers import TicTacToeConsumer
from django.urls import re_path



websocket_urlpatterns = [
    re_path(r'^ws/play/(?P<room_code>\w+)/$', TicTacToeConsumer.as_asgi()),
]