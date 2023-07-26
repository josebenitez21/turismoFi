from django.urls import path
from . import views

app_name = 'EjemploHighcharts'

urlpatterns = [
    path('', views.barras_check_view, name='barras_check'),
    path('obtener-datos/', views.obtener_datos, name='obtener_datos'),
    path('graficaNacionalAnual/', views.graficaNacionalAnual, name= 'graficaNacionalAnual'),
    path('dashb/',  views.dash_view, name ='dashB'),
]
