from django.http import JsonResponse
from django.db.models import Sum
from core.models import EstablecimientoRegistro
from django.shortcuts import render


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


def barras_check_view(request):
    return render(request, 'Graficas/barrasCheck.html')

def dash_view(request):
    return render(request, 'DashboardG.html')


