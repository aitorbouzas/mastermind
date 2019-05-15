from django.conf.urls import url
from game.views import game_list, game_detail

urlpatterns = [
    url(r'^game/$', game_list.GameList.as_view()),
    url(r'^game/(?P<id>[0-9a-f-]+)$', game_detail.GameDetail.as_view()),
]
