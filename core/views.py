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
        formulario = LoginForm(request.POST)
        if formulario.is_valid:
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

    ctx['form'] = LoginForm()

    return render(request, 'core/login.html', ctx)


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
