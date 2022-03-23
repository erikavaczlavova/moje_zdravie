from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('vaccine', views.vaccine, name='vaccine'),
    path('passport', views.passport, name='passport')

]