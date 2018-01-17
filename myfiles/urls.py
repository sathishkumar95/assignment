from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'myfiles'

urlpatterns = [
    path('',views.index,name='index'),
    path('data/',views.data,name='data'),
]