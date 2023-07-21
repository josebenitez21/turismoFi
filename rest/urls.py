from django.urls import path
from . import views

app_name = 'rest'
urlpatterns = [
    path('establecimientos/', views.establecimientos, name='rest_establecimientos'),
    path('registros/', views.registros, name='rest_registros'),
]
