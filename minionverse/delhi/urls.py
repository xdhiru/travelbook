from django.urls import path, include
from . import views

app_name='delhi'

urlpatterns = [
    path('', views.city, name='city'),
    path('cinemas/', views.cinemas, name='cinemas')

]
