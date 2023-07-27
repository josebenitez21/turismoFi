from django.urls import path
from . import views

app_name = 'EjemploHighcharts'

urlpatterns = [
    path('', views.barras_check_view, name='barras_check'),
    path('obtener-datos/', views.obtener_datos, name='obtener_datos'),
    path('obtener-anual', views.obtener_datosCheckinsAnuales, name='obtener_anuales'),
    path('checkoutsG/', views.obtener_datosCheckoutsGenerales, name='checkoutsG'),
    path('pernoctacionesAnuales/', views.obtener_datosPernoctacionesAnuales, name='pernoctacionesAnuales'),
    path('datosNacionalesAnual/', views.obtener_datosNacionalesAnual, name='datosNacionalesAnual'),
    path('datosExtranjerosAnual/', views.obtener_datosExtranjerosAnual, name='datosExtranjerosAnual'),

    path('obtener-datos-CheckAnuales/', views.obtener_datosExtranjerosAnual, name='obtener_datos_CheckinsAnuales'),
    path('dashb/', views.dash_view, name='dashB'),

]
