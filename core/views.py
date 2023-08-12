from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from core.forms import *
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm, ReCaptchaField


# Create your views here.
def _get_context(request):
    ctx = {}
    ctx['administrativo'] = False
    user = request.user
    gAdministrativos = Group.objects.get(name="ADMINISTRATIVOS")
    if user in gAdministrativos.user_set.all():
        ctx['administrativo'] = True
    return ctx


def index(request):
    ctx = _get_context(request)
    return render(request, 'core/index.html', ctx)


def login_view(request):
    ctx = {}
    if request.method == 'POST':
        formulario = LoginForm(request=request, data=request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave = request.POST['password']

            user = authenticate(username=usuario, password=clave)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(_group_user(user))
                else:
                    ctx['message'] = "Usuario en estado inactivo"
            else:
                ctx['message'] = "Usuario o clave incorrectos"
    else:
        formulario = LoginForm()

    ctx['form'] = formulario  # Usar el formulario instanciado

    return render(request, 'core/login.html', ctx)


def years_view(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)

    print(ctx)

    return render(request, 'core/DatosAnuales/DatosAnuales.html', ctx)


def _group_user(user):
    url = 'profile'

    if user.is_staff:
        url = '/admin'

    return url


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    ctx = {}
    return redirect('index')


@login_required(login_url='/login/')
def profile(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/profile.html', ctx)


@login_required(login_url='/login/')
def datosAnuales(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosAnuales/DatosAnuales.html', ctx)


# Redirect a datosAnual
@login_required(login_url='/login/')
def datosAnuales(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosAnuales/DatosAnuales.html', ctx)


@login_required(login_url='/login/')
def CheckinsA(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosAnuales/CheckinsA.html', ctx)


@login_required(login_url='/login/')
def CheckoutsA(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosAnuales/CheckoutA.html', ctx)


@login_required(login_url='/login/')
def ExtranjerosA(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosAnuales/ExtranjerosA.html', ctx)


@login_required(login_url='/login/')
def HabitacionesDisponiblesA(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosAnuales/HabitacionesDisponiblesA.html', ctx)


@login_required(login_url='/login/')
def HabitacionesOcupadasA(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosAnuales/HabitacionesOcupadasA.html', ctx)


@login_required(login_url='/login/')
def NacionalesA(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosAnuales/NacionalesA.html', ctx)


@login_required(login_url='/login/')
def PernoctacionesA(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosAnuales/PernoctacionesA.html', ctx)


@login_required(login_url='/login/')
def TarifaA(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosAnuales/TarifaA.html', ctx)


@login_required(login_url='/login/')
def VentasA(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosAnuales/VentasA.html', ctx)


@login_required(login_url='/login/')
def RevParA(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosAnuales/RevParA.html', ctx)


@login_required(login_url='/login/')
def OcupacionA(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosAnuales/OcupacionA.html', ctx)


@login_required(login_url='/login/')
def EmpleadosTA(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosAnuales/EmpleadosTA.html', ctx)


# Fin modelo 1

# redirect to DatosMensuales

# Inicio modelo 2
@login_required(login_url='/login/')
def datosMensuales(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosMensuales/DatosMensuales.html', ctx)


@login_required(login_url='/login/')
def CheckinsM(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosMensuales/CheckinsM.html', ctx)


@login_required(login_url='/login/')
def CheckoutsM(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosMensuales/CheckoutM.html', ctx)


@login_required(login_url='/login/')
def ExtranjerosM(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosMensuales/ExtranjerosM.html', ctx)


@login_required(login_url='/login/')
def HabitacionesDisponiblesM(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosMensuales/HabitacionesDisponiblesM.html', ctx)


@login_required(login_url='/login/')
def HabitacionesOcupadasM(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosMensuales/HabitacionesOcupadasM.html', ctx)


@login_required(login_url='/login/')
def NacionalesM(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosMensuales/NacionalesM.html', ctx)


@login_required(login_url='/login/')
def PernoctacionesM(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosMensuales/PernoctacionesM.html', ctx)


@login_required(login_url='/login/')
def TarifaM(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosMensuales/TarifaM.html', ctx)


@login_required(login_url='/login/')
def VentasM(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosMensuales/VentasM.html', ctx)


@login_required(login_url='/login/')
def RevParM(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosMensuales/RevParM.html', ctx)


@login_required(login_url='/login/')
def OcupacionM(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosMensuales/OcupacionM.html', ctx)

@login_required(login_url='/login/')
def EmpleadosTeM(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosMensuales/EmpleadosTM.html', ctx)

# Fin modelo 2

# Inicio modelo 3

@login_required(login_url='/login/')
def datosDiarios(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosDiarios/DatosDiarios.html', ctx)


@login_required(login_url='/login/')
def CheckinsD(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosDiarios/CheckinsD.html', ctx)


@login_required(login_url='/login/')
def CheckoutsD(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosDiarios/CheckoutD.html', ctx)


@login_required(login_url='/login/')
def ExtranjerosD(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosDiarios/ExtranjerosD.html', ctx)


@login_required(login_url='/login/')
def HabitacionesDisponiblesD(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosDiarios/HabitacionesDisponiblesD.html', ctx)


@login_required(login_url='/login/')
def HabitacionesOcupadasD(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosDiarios/HabitacionesOcupadasD.html', ctx)


@login_required(login_url='/login/')
def NacionalesD(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosDiarios/NacionalesD.html', ctx)


@login_required(login_url='/login/')
def PernoctacionesD(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosDiarios/PernoctacionesD.html', ctx)


@login_required(login_url='/login/')
def TarifaD(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosDiarios/TarifaD.html', ctx)


@login_required(login_url='/login/')
def VentasD(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosDiarios/VentasD.html', ctx)


@login_required(login_url='/login/')
def RevParD(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosDiarios/RevParD.html', ctx)


@login_required(login_url='/login/')
def OcupacionD(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosDiarios/OcupacionD.html', ctx)

@login_required(login_url='/login/')
def EmpleadosTeD(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'core/DatosDiarios/EmpleadosTeD.html', ctx)

# Fin modelo 3

@login_required(login_url='/login/')
def views_years(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    print('Hola')
    return render(request, 'core/DatosDiarios/DatosDiarios.html', ctx)


@login_required(login_url='/login/')
def establecimientos(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'establecimiento/list.html', ctx)


@login_required(login_url='/login/')
def establecimientos(request):
    ctx = _get_context(request)
    user = request.user
    if ctx['administrativo']:
        # ctx['list'] = Establecimiento.objects.all()
        provincias = _get_provincias(user)
        ctx['list'] = Establecimiento.objects.filter(provincia__in=provincias)
    else:
        ctx['list'] = Establecimiento.objects.filter(user=user)
    return render(request, 'establecimiento/list.html', ctx)


@login_required(login_url='/login/')
def establecimiento(request, id):
    ctx = _get_context(request)
    user = request.user
    ctx['item'] = Establecimiento.objects.get(id=id)
    return render(request, 'establecimiento/view.html', ctx)


@login_required(login_url='/login/')
def establecimiento_nuevo(request):
    ctx = _get_context(request)
    user = request.user
    if request.method == 'POST':
        form = EstablecimientoForm(user.id, request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:profile')
    else:
        form = EstablecimientoForm(user.id)

    ctx['form'] = form

    return render(request, 'establecimiento/object.html', {'form': form})


@login_required(login_url='/login/')
def establecimiento_editar(request, id):
    user = request.user
    est = Establecimiento.objects.get(id=id)
    if request.method == 'POST':
        form = EstablecimientoEditarForm(user.id, request.POST, instance=est)
        if form.is_valid():
            form.save()
            return redirect('core:establecimiento', id=id)
    else:
        form = EstablecimientoEditarForm(user.id, instance=est)

    ctx = {'form': form, 'item': est, 'action': 'editar'}

    return render(request, 'establecimiento/object.html', ctx)


@login_required(login_url='/login/')
def establecimiento_registros(request, id):
    ctx = _get_context(request)
    est = Establecimiento.objects.get(id=id)
    ctx['list'] = EstablecimientoRegistro.objects.filter(establecimiento=est)
    ctx['item'] = est
    return render(request, 'establecimiento/registers.html', ctx)


@login_required(login_url='/login/')
def establecimiento_registro_nuevo(request, id):
    est = Establecimiento.objects.get(id=id)
    if request.method == 'POST':
        form = EstablecimientoRegistroForm(est.id, request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.porcentaje_ocupacion = (Decimal(obj.habitaciones_ocupadas) / Decimal(
                obj.establecimiento.habitaciones)) * Decimal(100.0)
            obj.revpar = Decimal(obj.ventas_netas) / Decimal(obj.establecimiento.habitaciones)
            obj.save()
            return redirect('core:establecimiento_registros', id=id)
    else:
        form = EstablecimientoRegistroForm(est.id)

    ctx = {'form': form, 'item': est}

    return render(request, 'establecimiento/register.html', ctx)


@login_required(login_url='/login/')
def establecimiento_registro_editar(request, id):
    reg = EstablecimientoRegistro.objects.get(id=id)
    if request.method == 'POST':
        form = EstablecimientoRegistroForm(reg.establecimiento.id, request.POST, instance=reg)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.porcentaje_ocupacion = (Decimal(obj.habitaciones_ocupadas) / Decimal(
                obj.establecimiento.habitaciones)) * Decimal(100.0)
            obj.revpar = Decimal(obj.ventas_netas) / Decimal(obj.establecimiento.habitaciones)
            obj.save()
            return redirect('core:establecimiento_registros', id=reg.establecimiento.id)
    else:
        form = EstablecimientoRegistroForm(reg.establecimiento.id, instance=reg)

    ctx = {'form': form, 'item': reg.establecimiento}

    return render(request, 'establecimiento/register.html', ctx)


@login_required(login_url='/login/')
def establecimiento_registro_eliminar(request, id):
    ctx = _get_context(request)
    reg = EstablecimientoRegistro.objects.get(id=id)
    est = reg.establecimiento
    reg.delete()
    return redirect('core:establecimiento_registros', id=est.id)


@login_required(login_url='/login/')
def registros(request):
    ctx = _get_context(request)
    # ctx['item'] = None
    if ctx['administrativo']:
        # ctx['list'] = EstablecimientoRegistro.objects.all()
        provincias = _get_provincias(request.user)
        ctx['list'] = EstablecimientoRegistro.objects.filter(establecimiento__provincia__in=provincias)
    else:
        ctx['list'] = EstablecimientoRegistro.objects.filter(establecimiento__user=request.user)
    return render(request, 'establecimiento/registers.html', ctx)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Se puede borrar el jsonp y cambiarlo por render_to_json_response

def jsonp(f):
    """Wrap a json response in a callback, and set the mimetype (Content-Type) header accordingly
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
            resp.content = "%s(%s)" % (callback, resp.content)
            return resp
        elif 'jsonp' in request.GET:
            callback = request.GET['jsonp']
            resp['Content-Type'] = 'text/javascript; charset=utf-8'
            resp.content = "%s(%s)" % (callback, resp.content)
            return resp
        else:
            return resp

    return jsonp_wrapper


@csrf_exempt
@jsonp
def validar(request):
    data = {}
    estado = ''
    if request.is_ajax() and request.method == 'POST':
        reg = EstablecimientoRegistro.objects.get(id=request.POST['id'])
        reg.estado = request.POST['estado']
        reg.save()
        estado = reg.estado

    data['result'] = estado

    return JsonResponse(data)


# utilities

def _get_provincias(user):
    provincias = []
    query = [provincias.extend(p.provincias.all()) for p in [obj for obj in user.user_provincia.all()]]
    return provincias

# end viewsp.py
# Create your views here.
