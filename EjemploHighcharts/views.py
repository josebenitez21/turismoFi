from django.http import JsonResponse
from django.db.models import Sum
from core.models import EstablecimientoRegistro
from django.shortcuts import render
from django.db.models.functions import Coalesce


def obtener_datos(request):
    user = request.user  # Obtener el usuario loggeado

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    datos = EstablecimientoRegistro.objects.filter(establecimiento__user=user)

    if year_param:
        datos = datos.filter(fecha__year=year_param)

    datos = datos.values('fecha__month').annotate(total_checkouts=Sum('checkouts'))

    meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]

    data = {
        'meses': [],
        'checkouts': [],
    }

    for mes_num in range(1, 13):
        mes = meses[mes_num - 1]
        data['meses'].append(mes)
        checkouts_mes = next((item['total_checkouts'] for item in datos if item['fecha__month'] == mes_num), 0)
        data['checkouts'].append(checkouts_mes)

    return JsonResponse(data)
def obtener_datosCheckinsAnuales(request):
    user = request.user  # Obtener el usuario loggeado

    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'checkins': [],  # Cambiar 'nacionales' por 'checkins' en el diccionario de datos
    }

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year__in=anios)

    if year_param:
        registros = registros.filter(fecha__year=year_param)

    # Cambiar el campo 'nacionales' por 'checkins' en el annotate para sumar los checkins en lugar de los nacionales
    registros = registros.values('fecha__year').annotate(total_checkins=Sum('checkins'))

    for anio in anios:
        # Cambiar 'total_nacionales' por 'total_checkins' para obtener la suma de los checkins
        checkins_anio = next(
            (registro['total_checkins'] for registro in registros if registro['fecha__year'] == anio), 0)
        data['checkins'].append(checkins_anio)  # Cambiar 'nacionales' por 'checkins' en la lista de datos

    return JsonResponse(data)


def obtener_datosCheckoutsGenerales(request):
    user = request.user  # Obtener el usuario loggeado

    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'checkouts': [],
    }

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year__in=anios)

    if year_param:
        registros = registros.filter(fecha__year=year_param)

    registros = registros.values('fecha__year').annotate(total_checkouts=Sum('checkouts'))

    for anio in anios:
        checkouts_anio = next(
            (registro['total_checkouts'] for registro in registros if registro['fecha__year'] == anio), 0)
        data['checkouts'].append(checkouts_anio)

    return JsonResponse(data)


def obtener_datosPernoctacionesAnuales(request):
    user = request.user  # Obtener el usuario loggeado

    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'pernoctaciones': [],
    }

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year__in=anios)

    if year_param:
        registros = registros.filter(fecha__year=year_param)

    registros = registros.values('fecha__year').annotate(total_pernoctaciones=Sum('pernoctaciones'))

    for anio in anios:
        pernoctaciones_anio = next(
            (registro['total_pernoctaciones'] for registro in registros if registro['fecha__year'] == anio), 0)
        data['pernoctaciones'].append(pernoctaciones_anio)

    return JsonResponse(data)
def obtener_datosNacionalesAnual(request):
    user = request.user  # Obtener el usuario loggeado

    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'nacionales': [],
    }

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year__in=anios)

    if year_param:
        registros = registros.filter(fecha__year=year_param)

    registros = registros.values('fecha__year').annotate(total_nacionales=Sum('nacionales'))

    for anio in anios:
        nacionales_anio = next(
            (registro['total_nacionales'] for registro in registros if registro['fecha__year'] == anio), 0)
        data['nacionales'].append(nacionales_anio)

    return JsonResponse(data)
def obtener_datosExtranjerosAnual(request):
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
    user = request.user  # Obtener el usuario loggeado

    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'habitaciones_ocupadas': [],
    }

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year__in=anios)

    if year_param:
        registros = registros.filter(fecha__year=year_param)

    registros = registros.values('fecha__year').annotate(total_habitaciones=Sum('habitaciones_ocupadas'))

    for anio in anios:
        habitaciones_ocupadas_anio = next(
            (registro['total_habitaciones'] for registro in registros if registro['fecha__year'] == anio), 0)

        data['habitaciones_ocupadas'].append(habitaciones_ocupadas_anio)

    return JsonResponse(data)


def obtener_datosHabitacionesDisponiblesAnual(request):
    user = request.user  # Obtener el usuario loggeado

    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'habitaciones_disponibles': [],
    }

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year__in=anios)

    if year_param:
        registros = registros.filter(fecha__year=year_param)

    registros = registros.values('fecha__year').annotate(total_habitaciones=Sum('habitaciones_disponibles'))

    for anio in anios:
        habitaciones_disponibles_anio = next(
            (registro['total_habitaciones'] for registro in registros if registro['fecha__year'] == anio), 0)

        data['habitaciones_disponibles'].append(habitaciones_disponibles_anio)

    return JsonResponse(data)
#revisar
def obtener_datosTarifaPromedioAnual(request):
    user = request.user  # Obtener el usuario loggeado

    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'tarifa_promedio': [],
    }

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year__in=anios)

    if year_param:
        registros = registros.filter(fecha__year=year_param)

    registros = registros.values('fecha__year').annotate(total_tarifa_promedio=Sum('tarifa_promedio'))

    for anio in anios:
        tarifa_promedio_anio = next(
            (registro['total_tarifa_promedio'] for registro in registros if registro['fecha__year'] == anio), 0)

        data['tarifa_promedio'].append(tarifa_promedio_anio)

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

def obtener_datosCheckinsMensuales(request):
    user = request.user  # Obtener el usuario loggeado

    # Obtener el año seleccionado desde el frontend
    year_param = request.GET.get('year')

    # Filtrar los registros del usuario por el año seleccionado
    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year=year_param) if year_param else EstablecimientoRegistro.objects.filter(establecimiento__user=user)

    # Agrupar por mes y sumar los checkins
    datos = registros.values('fecha__month').annotate(checkins=Sum('checkins'))

    meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]

    data = {
        'meses': [],
        'checkins': [],
    }

    for mes_num in range(1, 13):  # Rango de meses (1 a 12)
        mes = meses[mes_num - 1]
        data['meses'].append(mes)

        # Obtener el valor de checkins para el mes actual, si no hay valor, agregar 0
        checkins_mes = next((item['checkins'] for item in datos if item['fecha__month'] == mes_num), 0)
        data['checkins'].append(checkins_mes)

    return JsonResponse(data)

def obtener_datosCheckoutsMensuales(request):
    user = request.user  # Obtener el usuario loggeado

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    datos = EstablecimientoRegistro.objects.filter(establecimiento__user=user)

    if year_param:
        datos = datos.filter(fecha__year=year_param)

    datos = datos.values('fecha__month').annotate(total_checkouts=Sum('checkouts'))

    meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]

    data = {
        'meses': [],
        'checkouts': [],
    }

    for mes_num in range(1, 13):
        mes = meses[mes_num - 1]
        data['meses'].append(mes)
        checkouts_mes = next((item['total_checkouts'] for item in datos if item['fecha__month'] == mes_num), 0)
        data['checkouts'].append(checkouts_mes)

    return JsonResponse(data)
def barras_check_view(request):
    return render(request, 'Graficas/barrasCheck.html')

def graficaNacionalAnual(request):
    return render(request, 'Graficas/NacionalesAnual.html')


def dash_view(request):
    return render(request, 'DashboardG.html')


