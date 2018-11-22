from django.urls import path

from . import views

urlpatterns = [
    path('/byebye', views.byebye, name='byebye'),
]
