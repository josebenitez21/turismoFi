from django.http import JsonResponse
from django.db.models import Sum
from core.models import EstablecimientoRegistro
from django.shortcuts import render
from django.db.models.functions import Coalesce
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from core.views import profile
def obtener_datos(request):
    datos = EstablecimientoRegistro.objects.values('fecha__month') \
        .annotate(checkins=Sum('checkins'), checkouts=Sum('checkouts'))

    meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]

    data = {
        'meses': [],
        'checkins': [],
        'checkouts': []
    }


    datos_ordenados = sorted(datos, key=lambda x: x['fecha__month'])

    for item in datos_ordenados:
        mes_num = item['fecha__month']
        mes = meses[mes_num - 1]
        data['meses'].append(mes)
        data['checkins'].append(item['checkins'])
        data['checkouts'].append(item['checkouts'])


    return JsonResponse(data)

def obtener_datosCheckinsAnuales(request):
    datos = EstablecimientoRegistro.objects.filter(fecha__year__range=[2019, 2023]) \
        .values('fecha__year').annotate(checkins=Sum('checkins'))

    anios = list(range(2019, 2024))

    data = {
        'anios': [],
        'checkins': [],
    }

    for anio in anios:
        data['anios'].append(str(anio))
        checkins = next((item['checkins'] for item in datos if item['fecha__year'] == anio), 0)
        data['checkins'].append(checkins)

    return JsonResponse(data)

def obtener_datosCheckoutsGenerales(request):
    datos = EstablecimientoRegistro.objects.filter(fecha__year__range=[2019, 2023]) \
        .values('fecha__year').annotate(checkouts=Sum('checkouts'))

    anios = list(range(2019, 2024))

    data = {
        'anios': [],
        'checkouts': [],
    }

    for anio in anios:
        data['anios'].append(str(anio))
        checkouts = next((item['checkouts'] for item in datos if item['fecha__year'] == anio), 0)
        data['checkouts'].append(checkouts)

    return JsonResponse(data)


def obtener_datosPernoctacionesAnuales(request):
    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'pernoctaciones': [],
    }

    registros = EstablecimientoRegistro.objects.filter(fecha__year__in=anios) \
                                               .values('fecha__year') \
                                               .annotate(total_pernoctaciones=Sum('pernoctaciones'))

    for anio in anios:
        pernoctaciones_anio = next((registro['total_pernoctaciones'] for registro in registros if registro['fecha__year'] == anio), 0)
        data['pernoctaciones'].append(pernoctaciones_anio)

    return JsonResponse(data)

def obtener_datosNacionalesAnual(request):
    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'nacionales': [],
    }

    registros = EstablecimientoRegistro.objects.filter(fecha__year__in=anios) \
        .values('fecha__year') \
        .annotate(total_nacionales=Sum('nacionales'))

    for anio in anios:
        nacionales_anio = next(
            (registro['total_nacionales'] for registro in registros if registro['fecha__year'] == anio), 0)
        data['nacionales'].append(nacionales_anio)

    return JsonResponse(data)

def obtener_datosExtranjerosAnual(request):
    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'extranjeros': [],
    }

    registros = EstablecimientoRegistro.objects.filter(fecha__year__in=anios) \
        .values('fecha__year') \
        .annotate(total_extranjeros=Sum('extranjeros'))

    for anio in anios:
        extranjeros_anio = next(
            (registro['total_extranjeros'] for registro in registros if registro['fecha__year'] == anio), 0)
        data['extranjeros'].append(extranjeros_anio)

    return JsonResponse(data)

from django.db.models import Sum

def obtener_datosHabitacionesOcupadasAnual(request):
    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'habitaciones_ocupadas': [],
    }

    registros = EstablecimientoRegistro.objects.filter(fecha__year__in=anios) \
        .values('fecha__year') \
        .annotate(total_habitaciones=Sum('habitaciones_ocupadas'))

    for anio in anios:
        habitaciones_ocupadas_anio = next(
            (registro['total_habitaciones'] for registro in registros if registro['fecha__year'] == anio), 0)

        data['habitaciones_ocupadas'].append(habitaciones_ocupadas_anio)

    return JsonResponse(data)

from django.db.models import Sum

def obtener_datosHabitacionesDisponiblesAnual(request):
    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'habitaciones_disponibles': [],
    }

    registros = EstablecimientoRegistro.objects.filter(fecha__year__in=anios) \
        .values('fecha__year') \
        .annotate(total_habitaciones=Sum('habitaciones_disponibles'))

    for anio in anios:
        habitaciones_disponibles_anio = next(
            (registro['total_habitaciones'] for registro in registros if registro['fecha__year'] == anio), 0)

        data['habitaciones_disponibles'].append(habitaciones_disponibles_anio)

    return JsonResponse(data)
#revisar
def obtener_datosTarifaPromedioAnual(request):
    datos = EstablecimientoRegistro.objects.filter(fecha__year__range=[2019, 2023]) \
        .values('fecha__year').annotate(tarifa_promedio=Sum('tarifa_promedio'))

    anios = list(range(2019, 2024))

    data = {
        'anios': [],
        'tarifa_promedio': [],
    }

    for anio in anios:
        data['anios'].append(str(anio))
        checkins = next((item['tarifa_promedio'] for item in datos if item['fecha__year'] == anio), 0)
        data['tarifa_promedio'].append(checkins)

    return JsonResponse(data)
#revisar
def obtener_datosVentasNetasAnual(request):
    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'ventas_netas': [],
    }

    registros = EstablecimientoRegistro.objects.filter(fecha__year__in=anios) \
        .values('fecha__year') \
        .annotate(total_ventas_netas=Sum('ventas_netas'))

    for anio in anios:
        ventas_netas_anio = next(
            (registro['total_ventas_netas'] for registro in registros if registro['fecha__year'] == anio), 0)

        data['ventas_netas'].append(ventas_netas_anio)

    return JsonResponse(data)

def obtener_datosPorcentajeOcupacionAnual(request):
    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'porcentaje_ocupacion': [],
    }

    registros = EstablecimientoRegistro.objects.filter(fecha__year__in=anios) \
        .values('fecha__year') \
        .annotate(total_porcentaje_ocupacion=Sum('porcentaje_ocupacion'))

    for anio in anios:
        porcentaje_ocupacion_anio = next(
            (registro['total_porcentaje_ocupacion'] for registro in registros if registro['fecha__year'] == anio), 0)

        data['porcentaje_ocupacion'].append('porcentaje_ocupacion_anio')

    return JsonResponse(data)

def obtener_datosEmpleadosTemporalesAnual(request):
    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'empleados_temporales': [],
    }

    registros = EstablecimientoRegistro.objects.filter(fecha__year__in=anios) \
        .values('fecha__year') \
        .annotate(total_empleados_temporales=Sum('empleados_temporales'))

    for anio in anios:
        empleados_temporales_anio = next(
            (registro['total_empleados_temporales'] for registro in registros if registro['fecha__year'] == anio), 0)

        data['empleados_temporales'].append(empleados_temporales_anio)

    return JsonResponse(data)


def barras_check_view(request):
    return render(request, 'Graficas/barrasCheck.html')

def dash_view(request):
    return render(request, 'DashboardG.html')


