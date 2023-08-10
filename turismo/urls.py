from django.contrib import admin
from django.urls import include, path

import EjemploHighcharts.views
from core import views as core_views
from EjemploHighcharts import views
from EjemploHighcharts import views as ejhc_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', core_views.index, name='index'),
                  path('login/', core_views.login_view, name='login'),
                  path('logout/', core_views.logout_view, name='logout'),
                  path('accounts/profile/', core_views.profile, name='profile'),
                  path('core/', include('core.urls', namespace='core')),
                  path('rest/', include('rest.urls', namespace='rest')),
                  path('obtener-datos/', views.obtener_datos, name='obtener_datos'),
                  path('pernoctacionesAnuales/', views.obtener_datosPernoctacionesAnuales,
                       name='pernoctacionesAnuales'),
                  path('datosNacionalesAnual/', views.obtener_datosNacionalesAnual, name='datosNacionalesAnual'),
                  path('datosExtranjerosAnual/', views.obtener_datosExtranjerosAnual, name='datosExtranjerosAnual'),
                  path('datosHabiOcp/', views.obtener_datosHabitacionesOcupadasAnual, name='datosHabiOcp'),
                  path('datosHabiDis/', views.obtener_datosHabitacionesDisponiblesAnual, name='datosHabiDis'),
                  path('datosTarifaA/', views.obtener_datosTarifaPromedioAnual, name='datosTarifaA'),
                  path('datosCheckinsMensuales/', views.obtener_datosCheckinsMensuales, name='datosCheckinsMensuales'),
                  path('datosCheckoutMes/', views.obtener_datosCheckoutsMensuales, name='datosCheckoutMes'),
                  path('PernoctacionesMes/', views.obtener_datosPernoctacionesMensuales, name='PernoctacionesMes'),
                  path('NacionalMes/', views.obtener_datosNacionalesMensuales, name='NacionalMes'),
                  path('ExtranjerosMes/', views.obtener_datosExtranjerosMensuales, name='ExtranjerosMes'),
                  path('HabiOcMes/', views.obtener_datosHabitacionesOcupadasMensuales, name='HabiOcMes'),
                  path('HabiDisMes/', views.obtener_datosHabitacionesDisponiblesMensuales, name='HabiDisMes'),
                  path('HabiDisDia/', views.obtener_datosHabitacionesDisponiblesDiarias, name='HabiDisDia'),
                  path('CheckinsDia/', views.obtener_datosCheckinsDiarios, name='CheckinsDia'),
                  path('CheckoutsDia/', views.obtener_datosCheckoutsDiario, name='CheckoutsDia'),
                  path('PernoctacionesDia/', views.obtener_datosPernoctacionesDias, name='PernoctacionesDia'),
                  path('NacionalesDia/', views.obtener_datosNacionalesDia, name='NacionalesDia'),
                  path('ExtranjerosDia/', views.obtener_datosExtranjerosDia, name='ExtranjerosDia'),
                  path('HabiOcDia/', views.obtener_datosHabitacionesOcupadas, name='HabiOcDia'),
                  path('anuales', core_views.views_years, name='years_view'),
                  path('datosCheckinsAnuales/', views.obtener_datosCheckinsAnuales, name='datosCheckinsAnuales'),
                  path('checkoutsG/', views.obtener_datosCheckoutsGenerales, name='checkoutsG'),
                  path('datosMensuales/', views.obtener_datosCheckinsMensuales, name='datosMensuales'),
                  path('datosDiarios/', views.obtener_datosCheckinsDiarios, name='datosDiarios'),
                  path('obtener_NacionalAnual/', views.graficaNacionalAnual, name='graficaNacionalAnual'),
                  path('ejemplohighcharts/', include('EjemploHighcharts.urls')),
                  path('accounts/profile/DatosAnuales', core_views.datosAnuales, name='DatosAnuales'),
                  path('accounts/profile/CheckinsA', core_views.CheckinsA, name='CheckinsA'),
                  path('accounts/profile/CheckoutsA', core_views.CheckoutsA, name='CheckoutsA'),
                  path('accounts/profile/ExtranjerosA', core_views.ExtranjerosA, name='ExtranjerosA'),
                  path('accounts/profile/HabiDisA', core_views.HabitacionesDisponiblesA, name='HabiDisA'),
                  path('accounts/profile/HabiOcA', core_views.HabitacionesOcupadasA, name='HabiOcA'),
                  path('accounts/profile/NacionalesA', core_views.NacionalesA, name='NacionalesA'),
                  path('accounts/profile/PernoctacionesA', core_views.PernoctacionesA, name='PernoctacionesA'),
                  path('accounts/profile/DatosMensuales', core_views.datosMensuales, name='DatosMensuales'),
                  path('accounts/profile/CheckinsM', core_views.CheckinsM, name='CheckinsM'),
                  path('accounts/profile/CheckoutsM', core_views.CheckoutsM, name='CheckoutsM'),
                  path('accounts/profile/ExtranjerosM', core_views.ExtranjerosM, name='ExtranjerosM'),
                  path('accounts/profile/HabiDisM', core_views.HabitacionesDisponiblesM, name='HabiDisM'),
                  path('accounts/profile/HabiOcM', core_views.HabitacionesOcupadasM, name='HabiOcM'),
                  path('accounts/profile/NacionalesM', core_views.NacionalesM, name='NacionalesM'),
                  path('accounts/profile/PernoctacionesM', core_views.PernoctacionesM, name='PernoctacionesM'),
                  path('accounts/profile/DatosDiarios', core_views.datosDiarios, name='DatosDiarios'),
                  path('accounts/profile/CheckinsD', core_views.CheckinsD, name='CheckinsD'),
                  path('accounts/profile/CheckoutsD', core_views.CheckoutsD, name='CheckoutsD'),
                  path('accounts/profile/ExtranjerosD', core_views.ExtranjerosD, name='ExtranjerosD'),
                  path('accounts/profile/HabiDisD', core_views.HabitacionesDisponiblesD, name='HabiDisD'),
                  path('accounts/profile/HabiOcD', core_views.HabitacionesOcupadasD, name='HabiOcD'),
                  path('accounts/profile/NacionalesD', core_views.NacionalesD, name='NacionalesD'),
                  path('accounts/profile/PernoctacionesD', core_views.PernoctacionesD, name='PernoctacionesD'),

                  path('estadistica/', TemplateView.as_view(template_name='Estadistica.html'), name='estadistica'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
