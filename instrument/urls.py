from django.conf.urls import url
from . import views

app_name = 'instrument'

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^logi/$', views.logi, name='logi'),#登入
    url(r'^logo/$', views.logo, name='logo'),#登出
    url(r'^register/$', views.register, name='register'),#注册
    url(r'^(?P<instrument_id>[0-9]+)/$', views.order, name='order'),#预约详情
    url(r'^(?P<instrument_id>[0-9]+)/add/$', views.add, name='add'),#添加预约
    url(r'^(?P<instrument_id>[0-9]+)/(?P<order_id>[0-9]+)/$', views.delete, name='delete'),#删除预约
    url(r'^my_order/$', views.my_order, name='my_order'),
]