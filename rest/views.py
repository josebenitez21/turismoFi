from django.http import JsonResponse
from core.forms import *
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


def jsonp(f):
    """
    Wrap a json response in a callback, and set the mimetype (Content-Type) header accordingly
    (will wrap in text/javascript if there is a callback). If the "callback" or "jsonp" paramters
    are provided, will wrap the json output in callback({thejson})

    Usage:

    @jsonp
    def my_json_view(request):
        d = { 'key': 'value' }
        return HTTPResponse(json.dumps(d), content_type='application/json')

    """
    from functools import wraps

    @wraps(f)
    def jsonp_wrapper(request, *args, **kwargs):
        resp = f(request, *args, **kwargs)
        if resp.status_code != 200:
            return resp
        if 'callback' in request.GET:
            callback = request.GET['callback']
            resp['Content-Type'] = 'text/javascript; charset=utf-8'
            resp.content = f'{callback}({resp.content})'
            return resp
        elif 'jsonp' in request.GET:
            callback = request.GET['jsonp']
            resp['Content-Type'] = 'text/javascript; charset=utf-8'
            resp.content = f'{callback}({resp.content})'
            return resp
        else:
            return resp

    return jsonp_wrapper


@ensure_csrf_cookie
@jsonp
def establecimientos(request):
    data = {}
    data['version'] = '1.0'
    data['name'] = 'Establecimientos'
    data['description'] = 'Establecimientos'
    data['lista'] = []

    try:
        token = request.GET['Authorization']
    except:
        token = None

    if token == 'Token 612893sjksshjk87178ahma91':
        try:
            start = int(request.GET['start'])
        except:
            start = 0
        try:
            limit = int(request.GET['limit'])
        except:
            limit = 100

        datos = Establecimiento.objects.all()
        data['count'] = len(datos)
        end = start + limit
        establecimientos = datos[start:end]
        data['base'] = 'limit={0}&start={1}'.format(limit, start)
        data['next'] = 'limit={0}&start={1}'.format(limit, end)
        for obj in establecimientos:
            aux = {}
            aux['uuid'] = f'EST{obj.id}'
            aux['establecimiento'] = obj.nombre
            if obj.clasificacion:
                aux['clasificacion'] = obj.clasificacion.nombre
            else:
                aux['clasificacion'] = ''
            if obj.categoria:
                aux['categoria'] = obj.categoria.nombre
            else:
                aux['categoria'] = ''
            if obj.provincia:
                aux['provincia'] = obj.provincia.nombre
            else:
                aux['provincia'] = ''
            if obj.canton:
                aux['canton'] = obj.canton.nombre
            else:
                aux['canton'] = ''
            if obj.parroquia:
                aux['parroquia'] = obj.parroquia.nombre
            else:
                aux['parroquia'] = ''

            aux['registro_SIIT'] = obj.registro_SIIT
            aux['registro_SIETE'] = obj.registro_SIETE
            aux['RUC'] = obj.RUC
            aux['email'] = obj.email
            aux['web'] = obj.web
            aux['telefono'] = obj
            aux['telefono'] = obj.telefono
            aux['direccion'] = obj.direccion
            aux['calle_principal'] = obj.calle_principal
            aux['calle_numero'] = obj.calle_numero
            aux['calle_secundaria'] = obj.calle_secundaria
            aux['empleados'] = obj.empleados
            aux['hombres'] = obj.hombres
            aux['mujeres'] = obj.mujeres
            aux['discapacitados'] = obj.discapacitados
            aux['empleados_habitaciones'] = obj.empleados_habitaciones
            aux['empleados_alimentos_bebidas'] = obj.empleados_alimentos_bebidas
            aux['empleados_administrativos'] = obj.empleados_administrativos
            aux['empleados_otras_areas'] = obj.empleados_otras_areas
            aux['local'] = obj.local
            aux['area_total'] = obj.area_total
            aux['area_alimentos_bebidas'] = obj.area_alimentos_bebidas
            aux['area_total'] = obj.area_total
            aux['habitaciones'] = obj.habitaciones
            aux['plazas'] = obj.plazas
            aux['propietario'] = obj.propietario
            aux['propietario'] = obj.propietario
            aux['representante'] = obj.representante
            aux['latitud'] = obj.latitud
            aux['longitud'] = obj.longitud
            data['lista'].append(aux)

        return JsonResponse(data, content_type='application/json')


@csrf_exempt
@jsonp
def registros(request):
    data = {}

    data['version'] = '1.0'
    data['name'] = 'Registros'
    data['description'] = 'Registros de ocupación hotelera'
    data['lista'] = []

    try:
        token = request.GET['Authorization']
    except:
        token = None

    if token == 'Token 612893sjksshjk87178ahma91':
        try:
            start = int(request.GET['start'])
        except:
            start = 0
        try:
            limit = int(request.GET['limit'])
        except:
            limit = 100

        registros = EstablecimientoRegistro.objects.all()
        data['count'] = len(registros)
        end = start + limit
        registros = registros[start:end]
        data['base'] = 'limit={0}&start={1}'.format(limit, start)
        data['next'] = 'limit={0}&start={1}'.format(limit, end)
        for obj in registros:
            aux = {}
            aux['uuid'] = f'EST{obj.establecimiento.id}'
            aux['establecimiento'] = obj.establecimiento.nombre
            aux['fecha'] = obj.fecha.strftime('%d-%m-%Y')
            aux['checkins'] = obj.checkins
            aux['checkouts'] = obj.checkouts
            aux['pernoctaciones'] = obj.pernoctaciones
            aux['nacionales'] = obj.nacionales
            aux['extranjeros'] = obj.extranjeros
            aux['habitaciones_ocupadas'] = obj.habitaciones_ocupadas
            aux['habitaciones_disponibles'] = obj.habitaciones_disponibles
            aux['tipo_tarifa'] = obj.tipo_tarifa.nombre
            aux['tarifa_promedio'] = '%s' % obj.tarifa_promedio
            aux['ventas_netas'] = '%s' % obj.ventas_netas
            aux['porcentaje_ocupacion'] = '%s' % obj.porcentaje_ocupacion
            aux['revpar'] = '%s' % obj.revpar
            aux['empleados_temporales'] = obj.empleados_temporales
            aux['estado'] = obj.estado
            aux['register'] = '%s' % obj.register.strftime('%d-%m-%Y')
            data['lista'].append(aux)

        return JsonResponse(data, content_type='application/json')
# end rest/views.py
