from django.conf.urls import url
from . import views

app_name = 'homeai'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]