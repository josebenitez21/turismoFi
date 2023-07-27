from django.urls import path
from core import views
app_name = 'core'
urlpatterns = [
    # path('orcid/', orcid, name='orcid'),
    path('establecimiento/<int:id>/', views.establecimiento, name='establecimiento'),
    path('establecimiento/nuevo/', views.establecimiento_nuevo, name='establecimiento_nuevo'),
    path('establecimiento/editar/<int:id>/', views.establecimiento_editar, name='establecimiento_editar'),
    path('establecimiento/registros/<int:id>/', views.establecimiento_registros, name='establecimiento_registros'),
    path('establecimiento/registro/nuevo/<int:id>/', views.establecimiento_registro_nuevo,
         name='establecimiento_registro_nuevo'),
    path('establecimiento/registro/editar/<int:id>/', views.establecimiento_registro_editar,
         name='establecimiento_registro_editar'),
    path('establecimiento/registro/eliminar/<int:id>/', views.establecimiento_registro_eliminar,
         name='establecimiento_registro_eliminar'),
    path('establecimientos/', views.establecimientos, name='establecimientos'),
    path('registros/', views.registros, name='registros'),
    path('validar/', views.validar, name='validar'),
    path('anuales', views.years_view, name='years_view')
]
