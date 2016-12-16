from django.conf.urls import url
from . import views

app_name = 'instrument'

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^logi/$', views.logi, name='logi'),#登入
    url(r'^logo/$', views.logo, name='logo'),#登出
    url(r'^register/$', views.register, name='register'),#注册
]