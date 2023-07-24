from django.contrib import admin
from django.urls import include, path
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
                  path('ejemplohighcharts/', include('EjemploHighcharts.urls')),
                  path('datos-anuales/', TemplateView.as_view(template_name='datos-anuales.html'),
                       name='datos-anuales'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
