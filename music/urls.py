from django.conf.urls import url
from . import views

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/id/ or /music/<album_id>
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),

    # /music/id/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),
]