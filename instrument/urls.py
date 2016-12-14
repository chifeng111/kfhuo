from django.conf.urls import url
from . import views

app_name = 'instrument'

urlpatterns = [
    url(r'^$', views.list, name='list')
]