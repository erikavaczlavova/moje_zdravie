from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('what', views.test, name='test'),
]