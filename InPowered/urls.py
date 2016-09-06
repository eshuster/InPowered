from django.conf.urls import url
from . import views
from . import models

app_name = 'InPowered'
urlpatterns = [
  url(r'^$', views.index, name='index'),
   url(r'^parse_url/$', views.parse_url, name='parse_url'),
]