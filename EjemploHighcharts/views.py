from django.http import JsonResponse
from django.db.models import Sum, Avg, Max, Min
from core.models import EstablecimientoRegistro
from django.shortcuts import render
from django.db.models.functions import Coalesce


def obtener_datos(request):
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





def barras_check_view(request):
    return render(request, 'Graficas/barrasCheck.html')


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
    user = request.user

    anios = list(range(2019, 2024))
    data = {
        'anios': anios,
        'extranjeros': [],
    }

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year__in=anios)

    if year_param:
        registros = registros.filter(fecha__year=year_param)

    registros = registros.values('fecha__year').annotate(total_extranjeros=Sum('extranjeros'))

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


# revisar
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


# revisar
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
    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user,
                                                       fecha__year=year_param) if year_param else EstablecimientoRegistro.objects.filter(
        establecimiento__user=user)

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


def obtener_datosPernoctacionesMensuales(request):
    user = request.user  # Obtener el usuario loggeado

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    datos = EstablecimientoRegistro.objects.filter(establecimiento__user=user)

    if year_param:
        datos = datos.filter(fecha__year=year_param)

    datos = datos.values('fecha__month').annotate(total_pernoctaciones=Sum('pernoctaciones'))

    meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]

    data = {
        'meses': [],
        'pernoctaciones': [],
    }

    for mes_num in range(1, 13):
        mes = meses[mes_num - 1]
        data['meses'].append(mes)
        pernoctaciones_mes = next((item['total_pernoctaciones'] for item in datos if item['fecha__month'] == mes_num),
                                  0)
        data['pernoctaciones'].append(pernoctaciones_mes)

    return JsonResponse(data)


def obtener_datosNacionalesMensuales(request):
    user = request.user  # Obtener el usuario loggeado

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    datos = EstablecimientoRegistro.objects.filter(establecimiento__user=user)

    if year_param:
        datos = datos.filter(fecha__year=year_param)

    datos = datos.values('fecha__month').annotate(total_nacionales=Sum('nacionales'))

    meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]

    data = {
        'meses': [],
        'nacionales': [],
    }

    for mes_num in range(1, 13):
        mes = meses[mes_num - 1]
        data['meses'].append(mes)
        nacionales_mes = next((item['total_nacionales'] for item in datos if item['fecha__month'] == mes_num), 0)
        data['nacionales'].append(nacionales_mes)

    return JsonResponse(data)


def obtener_datosExtranjerosMensuales(request):
    user = request.user  # Obtener el usuario loggeado

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    datos = EstablecimientoRegistro.objects.filter(establecimiento__user=user)

    if year_param:
        datos = datos.filter(fecha__year=year_param)

    datos = datos.values('fecha__month').annotate(total_extranjeros=Sum('extranjeros'))

    meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]

    data = {
        'meses': [],
        'extranjeros': [],
    }

    for mes_num in range(1, 13):
        mes = meses[mes_num - 1]
        data['meses'].append(mes)
        extranjeros_mes = next((item['total_extranjeros'] for item in datos if item['fecha__month'] == mes_num), 0)
        data['extranjeros'].append(extranjeros_mes)

    return JsonResponse(data)


def obtener_datosHabitacionesOcupadasMensuales(request):
    user = request.user  # Obtener el usuario loggeado

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    datos = EstablecimientoRegistro.objects.filter(establecimiento__user=user)

    if year_param:
        datos = datos.filter(fecha__year=year_param)

    datos = datos.values('fecha__month').annotate(total_habitaciones=Sum('habitaciones_ocupadas'))

    meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]

    data = {
        'meses': [],
        'habitaciones_ocupadas': [],
    }

    for mes_num in range(1, 13):
        mes = meses[mes_num - 1]
        data['meses'].append(mes)
        habitaciones_ocupadas_mes = next(
            (item['total_habitaciones'] for item in datos if item['fecha__month'] == mes_num), 0)
        data['habitaciones_ocupadas'].append(habitaciones_ocupadas_mes)

    return JsonResponse(data)


def obtener_datosHabitacionesDisponiblesMensuales(request):
    user = request.user  # Obtener el usuario loggeado

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend

    datos = EstablecimientoRegistro.objects.filter(establecimiento__user=user)

    if year_param:
        datos = datos.filter(fecha__year=year_param)

    datos = datos.values('fecha__month').annotate(total_habitaciones=Sum('habitaciones_disponibles'))

    meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]

    data = {
        'meses': [],
        'habitaciones_disponibles': [],
    }

    for mes_num in range(1, 13):
        mes = meses[mes_num - 1]
        data['meses'].append(mes)
        habitaciones_disponibles_mes = next(
            (item['total_habitaciones'] for item in datos if item['fecha__month'] == mes_num), 0)
        data['habitaciones_disponibles'].append(habitaciones_disponibles_mes)

    return JsonResponse(data)


def obtener_datosHabitacionesDisponiblesDiarias(request):
    user = request.user  # Obtener el usuario loggeado

    year_param = request.GET.get('year')  # Obtener el año seleccionado desde el frontend
    month_param = request.GET.get('month')  # Obtener el mes seleccionado desde el frontend

    datos = EstablecimientoRegistro.objects.filter(establecimiento__user=user)

    if year_param and int(year_param) in [2019, 2020, 2021, 2022, 2023]:
        datos = datos.filter(fecha__year=year_param)
    if month_param:
        datos = datos.filter(fecha__month=month_param)

    dias_del_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    data = {
        'dias': list(range(1, dias_del_mes[int(month_param) - 1] + 1)),
        'habitaciones_disponibles': [],
    }

    for dia in range(1, dias_del_mes[int(month_param) - 1] + 1):
        habitaciones_disponibles_dia = datos.filter(fecha__day=dia).aggregate(total=Sum('habitaciones_disponibles'))[
            'total']
        data['habitaciones_disponibles'].append(habitaciones_disponibles_dia or 0)

    return JsonResponse(data)


def obtener_datosCheckinsDiarios(request):
    user = request.user  # Obtener el usuario loggeado

    anios = [2019, 2020, 2021, 2022, 2023]
    year_param = int(request.GET.get('year', 0))  # Obtener el año seleccionado desde el frontend
    selected_year = year_param if year_param in anios else anios[-1]

    # Obtener el número de días de febrero según el año (considerando si es bisiesto o no)
    feb_days = 29 if (selected_year % 4 == 0 and selected_year % 100 != 0) or selected_year % 400 == 0 else 28

    meses = [
        {'nombre': 'Enero', 'dias': 31},
        {'nombre': 'Febrero', 'dias': feb_days},
        {'nombre': 'Marzo', 'dias': 31},
        {'nombre': 'Abril', 'dias': 30},
        {'nombre': 'Mayo', 'dias': 31},
        {'nombre': 'Junio', 'dias': 30},
        {'nombre': 'Julio', 'dias': 31},
        {'nombre': 'Agosto', 'dias': 31},
        {'nombre': 'Septiembre', 'dias': 30},
        {'nombre': 'Octubre', 'dias': 31},
        {'nombre': 'Noviembre', 'dias': 30},
        {'nombre': 'Diciembre', 'dias': 31},
    ]

    data = {
        'anios': anios,
        'selected_year': selected_year,
        'meses': meses,
        'checkins': [[] for _ in range(12)],  # Inicializar una lista vacía para cada mes
    }

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year=selected_year)

    for i, mes in enumerate(meses):
        for dia in range(1, mes['dias'] + 1):
            checkins_dia = registros.filter(fecha__month=i + 1, fecha__day=dia).aggregate(
                total_checkins=Sum('checkins'))
            total_checkins = checkins_dia['total_checkins'] if checkins_dia['total_checkins'] else 0
            data['checkins'][i].append(total_checkins)

    return JsonResponse(data)


def obtener_datosCheckoutsDiario(request):
    user = request.user  # Obtener el usuario loggeado

    anios = [2019, 2020, 2021, 2022, 2023]
    year_param = int(request.GET.get('year', 0))  # Obtener el año seleccionado desde el frontend
    selected_year = year_param if year_param in anios else anios[
        -1]  # Seleccionar el último año si no se proporciona uno válido

    # Obtener el número de días de febrero según el año (considerando si es bisiesto o no)
    feb_days = 29 if (selected_year % 4 == 0 and selected_year % 100 != 0) or selected_year % 400 == 0 else 28

    meses = [
        {'nombre': 'Enero', 'dias': 31},
        {'nombre': 'Febrero', 'dias': feb_days},
        {'nombre': 'Marzo', 'dias': 31},
        {'nombre': 'Abril', 'dias': 30},
        {'nombre': 'Mayo', 'dias': 31},
        {'nombre': 'Junio', 'dias': 30},
        {'nombre': 'Julio', 'dias': 31},
        {'nombre': 'Agosto', 'dias': 31},
        {'nombre': 'Septiembre', 'dias': 30},
        {'nombre': 'Octubre', 'dias': 31},
        {'nombre': 'Noviembre', 'dias': 30},
        {'nombre': 'Diciembre', 'dias': 31},
    ]

    data = {
        'anios': anios,
        'selected_year': selected_year,
        'meses': meses,
        'checkouts': [[] for _ in range(12)],  # Inicializar una lista vacía para cada mes
    }

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year=selected_year)

    for i, mes in enumerate(meses):
        for dia in range(1, mes['dias'] + 1):
            checkouts_dia = registros.filter(fecha__month=i + 1, fecha__day=dia).aggregate(
                total_checkouts=Sum('checkouts'))
            total_checkouts = checkouts_dia['total_checkouts'] if checkouts_dia['total_checkouts'] else 0
            data['checkouts'][i].append(total_checkouts)

    return JsonResponse(data)


def obtener_datosPernoctacionesDias(request):
    user = request.user

    anios = [2019, 2020, 2021, 2022, 2023]
    year_param = int(request.GET.get('year', 0))
    selected_year = year_param if year_param in anios else anios[-1]

    feb_days = 29 if (selected_year % 4 == 0 and selected_year % 100 != 0) or selected_year % 400 == 0 else 28

    meses = [
        {'nombre': 'Enero', 'dias': 31},
        {'nombre': 'Febrero', 'dias': feb_days},
        {'nombre': 'Marzo', 'dias': 31},
        {'nombre': 'Abril', 'dias': 30},
        {'nombre': 'Mayo', 'dias': 31},
        {'nombre': 'Junio', 'dias': 30},
        {'nombre': 'Julio', 'dias': 31},
        {'nombre': 'Agosto', 'dias': 31},
        {'nombre': 'Septiembre', 'dias': 30},
        {'nombre': 'Octubre', 'dias': 31},
        {'nombre': 'Noviembre', 'dias': 30},
        {'nombre': 'Diciembre', 'dias': 31},
    ]

    data = {
        'anios': anios,
        'selected_year': selected_year,
        'meses': meses,
        'pernoctaciones': [[] for _ in range(12)],  # Inicializar una lista vacía para cada mes
    }

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year=selected_year)

    for i, mes in enumerate(meses):
        for dia in range(1, mes['dias'] + 1):
            pernoctaciones_dia = registros.filter(fecha__month=i + 1, fecha__day=dia).aggregate(
                total_pernoctaciones=Sum('pernoctaciones'))
            total_pernoctaciones = pernoctaciones_dia['total_pernoctaciones'] if pernoctaciones_dia[
                'total_pernoctaciones'] else 0
            data['pernoctaciones'][i].append(total_pernoctaciones)

    return JsonResponse(data)


def obtener_datosNacionalesDia(request):
    user = request.user

    anios = [2019, 2020, 2021, 2022, 2023]
    year_param = int(request.GET.get('year', 0))
    selected_year = year_param if year_param in anios else anios[-1]

    feb_days = 29 if (selected_year % 4 == 0 and selected_year % 100 != 0) or selected_year % 400 == 0 else 28

    meses = [
        {'nombre': 'Enero', 'dias': 31},
        {'nombre': 'Febrero', 'dias': feb_days},
        {'nombre': 'Marzo', 'dias': 31},
        {'nombre': 'Abril', 'dias': 30},
        {'nombre': 'Mayo', 'dias': 31},
        {'nombre': 'Junio', 'dias': 30},
        {'nombre': 'Julio', 'dias': 31},
        {'nombre': 'Agosto', 'dias': 31},
        {'nombre': 'Septiembre', 'dias': 30},
        {'nombre': 'Octubre', 'dias': 31},
        {'nombre': 'Noviembre', 'dias': 30},
        {'nombre': 'Diciembre', 'dias': 31},
    ]

    data = {
        'anios': anios,
        'selected_year': selected_year,
        'meses': meses,
        'nacionales': [[] for _ in range(12)],  # Inicializar una lista vacía para cada mes
    }

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year=selected_year)

    for i, mes in enumerate(meses):
        for dia in range(1, mes['dias'] + 1):
            nacionales_dia = registros.filter(fecha__month=i + 1, fecha__day=dia).aggregate(
                total_nacionales=Sum('nacionales'))
            total_nacionales = nacionales_dia['total_nacionales'] if nacionales_dia['total_nacionales'] else 0
            data['nacionales'][i].append(total_nacionales)

    return JsonResponse(data)


def obtener_datosExtranjerosDia(request):
    user = request.user

    anios = [2019, 2020, 2021, 2022, 2023]
    year_param = int(request.GET.get('year', 0))
    selected_year = year_param if year_param in anios else anios[-1]

    feb_days = 29 if (selected_year % 4 == 0 and selected_year % 100 != 0) or selected_year % 400 == 0 else 28

    meses = [
        {'nombre': 'Enero', 'dias': 31},
        {'nombre': 'Febrero', 'dias': feb_days},
        {'nombre': 'Marzo', 'dias': 31},
        {'nombre': 'Abril', 'dias': 30},
        {'nombre': 'Mayo', 'dias': 31},
        {'nombre': 'Junio', 'dias': 30},
        {'nombre': 'Julio', 'dias': 31},
        {'nombre': 'Agosto', 'dias': 31},
        {'nombre': 'Septiembre', 'dias': 30},
        {'nombre': 'Octubre', 'dias': 31},
        {'nombre': 'Noviembre', 'dias': 30},
        {'nombre': 'Diciembre', 'dias': 31},
    ]

    data = {
        'anios': anios,
        'selected_year': selected_year,
        'meses': meses,
        'extranjeros': [[] for _ in range(12)],  # Inicializar una lista vacía para cada mes
    }

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year=selected_year)

    for i, mes in enumerate(meses):
        for dia in range(1, mes['dias'] + 1):
            extranjeros_dia = registros.filter(fecha__month=i + 1, fecha__day=dia).aggregate(
                total_extranjeros=Sum('extranjeros'))
            total_extranjeros = extranjeros_dia['total_extranjeros'] if extranjeros_dia['total_extranjeros'] else 0
            data['extranjeros'][i].append(total_extranjeros)

    return JsonResponse(data)


def obtener_datosHabitacionesOcupadas(request):
    user = request.user

    anios = [2019, 2020, 2021, 2022, 2023]
    year_param = int(request.GET.get('year', 0))
    selected_year = year_param if year_param in anios else anios[-1]

    feb_days = 29 if (selected_year % 4 == 0 and selected_year % 100 != 0) or selected_year % 400 == 0 else 28

    meses = [
        {'nombre': 'Enero', 'dias': 31},
        {'nombre': 'Febrero', 'dias': feb_days},
        {'nombre': 'Marzo', 'dias': 31},
        {'nombre': 'Abril', 'dias': 30},
        {'nombre': 'Mayo', 'dias': 31},
        {'nombre': 'Junio', 'dias': 30},
        {'nombre': 'Julio', 'dias': 31},
        {'nombre': 'Agosto', 'dias': 31},
        {'nombre': 'Septiembre', 'dias': 30},
        {'nombre': 'Octubre', 'dias': 31},
        {'nombre': 'Noviembre', 'dias': 30},
        {'nombre': 'Diciembre', 'dias': 31},
    ]

    data = {
        'anios': anios,
        'selected_year': selected_year,
        'meses': meses,
        'habitaciones_ocupadas': [[] for _ in range(12)],  # Inicializar una lista vacía para cada mes
    }

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year=selected_year)

    for i, mes in enumerate(meses):
        for dia in range(1, mes['dias'] + 1):
            habitaciones_ocupadas_dia = registros.filter(fecha__month=i + 1, fecha__day=dia).aggregate(
                total_habitaciones_ocupadas=Sum('habitaciones_ocupadas'))
            total_habitaciones_ocupadas = habitaciones_ocupadas_dia['total_habitaciones_ocupadas'] if \
            habitaciones_ocupadas_dia['total_habitaciones_ocupadas'] else 0
            data['habitaciones_ocupadas'][i].append(total_habitaciones_ocupadas)

    return JsonResponse(data)


def obtener_datosTarifaPromedioDias(request):
    user = request.user

    anios = [2019, 2020, 2021, 2022, 2023]
    year_param = int(request.GET.get('year', 0))
    selected_year = year_param if year_param in anios else anios[-1]

    feb_days = 29 if (selected_year % 4 == 0 and selected_year % 100 != 0) or selected_year % 400 == 0 else 28

    meses = [
        {'nombre': 'Enero', 'dias': 31},
        {'nombre': 'Febrero', 'dias': feb_days},
        {'nombre': 'Marzo', 'dias': 31},
        {'nombre': 'Abril', 'dias': 30},
        {'nombre': 'Mayo', 'dias': 31},
        {'nombre': 'Junio', 'dias': 30},
        {'nombre': 'Julio', 'dias': 31},
        {'nombre': 'Agosto', 'dias': 31},
        {'nombre': 'Septiembre', 'dias': 30},
        {'nombre': 'Octubre', 'dias': 31},
        {'nombre': 'Noviembre', 'dias': 30},
        {'nombre': 'Diciembre', 'dias': 31},
    ]

    data = {
        'anios': anios,
        'selected_year': selected_year,
        'meses': meses,
        'tarifa_promedio': [[] for _ in range(12)],  # Inicializar una lista vacía para cada mes
    }

    registros = EstablecimientoRegistro.objects.filter(establecimiento__user=user, fecha__year=selected_year)

    for i, mes in enumerate(meses):
        for dia in range(1, mes['dias'] + 1):
            tarifa_promedio_dia = registros.filter(fecha__month=i + 1, fecha__day=dia).aggregate(
                avg_tarifa=Sum('tarifa_promedio'))
            tarifa_promedio = tarifa_promedio_dia['avg_tarifa'] if tarifa_promedio_dia['avg_tarifa'] else 0
            data['tarifa_promedio'][i].append(round(tarifa_promedio, 2))  # Redondear a 2 decimales

    return JsonResponse(data)


def graficaNacionalAnual(request):
    return render(request, 'Graficas/NacionalesAnual.html')


def dash_view(request):
    return render(request, 'DashboardG.html')
