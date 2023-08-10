# -*- coding: utf-8 -*-

from django.utils.translation import gettext as _
from django import forms
from core.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import DateInput
from captcha.fields import ReCaptchaField
from datetime import datetime



class EstablecimientoForm(forms.ModelForm):

    def __init__(self, id, *args, **kwargs):
        super(EstablecimientoForm, self).__init__(*args, **kwargs)
        self.fields['user'] = forms.ModelChoiceField(queryset=User.objects.filter(id=id), initial=id,
                                                     widget=forms.HiddenInput())
        # self.fields['tipo'] = forms.ModelChoiceField(queryset = Items.objects.filter(catalogo_id=1))
        self.fields['clasificacion'] = forms.ModelChoiceField(queryset=Items.objects.filter(catalogo_id=2))
        self.fields['categoria'] = forms.ModelChoiceField(queryset=Items.objects.filter(catalogo_id=3))
        self.fields['tipo_tarifa'] = forms.ModelChoiceField(queryset=Items.objects.filter(catalogo_id=4))
        # self.fields['provincia'] = forms.ModelChoiceField(queryset = Items.objects.filter(catalogo_id=5))
        # self.fields['canton'] = forms.ModelChoiceField(queryset = Items.objects.filter(catalogo_id=6))
        # self.fields['parroquia'] = forms.ModelChoiceField(queryset = Items.objects.filter(catalogo_id=7))

    class Meta:
        model = Establecimiento
        exclude = ('register',)


class EstablecimientoEditarForm(forms.ModelForm):

    def __init__(self, id, *args, **kwargs):
        super(EstablecimientoEditarForm, self).__init__(*args, **kwargs)
        self.fields['user'] = forms.ModelChoiceField(queryset=User.objects.filter(id=id), initial=id,
                                                     widget=forms.HiddenInput())
        # self.fields['tipo'] = forms.ModelChoiceField(queryset = Items.objects.filter(catalogo_id=8))
        # self.fields['clasificacion'] = forms.ModelChoiceField(queryset = Items.objects.filter(catalogo_id=2))
        # self.fields['categoria'] = forms.ModelChoiceField(queryset = Items.objects.filter(catalogo_id=3))
        # self.fields['tipo_tarifa'] = forms.ModelChoiceField(queryset = Items.objects.filter(catalogo_id=4))
        self.fields['provincia'].widget.attrs['readonly'] = 'readonly'
        self.fields['canton'].widget.attrs['readonly'] = 'readonly'
        self.fields['parroquia'].widget.attrs['readonly'] = 'readonly'
        self.fields['RUC'].widget.attrs['readonly'] = 'readonly'
        self.fields['registro_SIIT'].widget.attrs['readonly'] = 'readonly'
        self.fields['registro_SIETE'].widget.attrs['readonly'] = 'readonly'
        self.fields['nombre'].widget.attrs['readonly'] = 'readonly'
        # self.fields['clasificacion'].widget.attrs['disabled'] = True
        # self.fields['categoria'].widget.attrs['disabled'] = True

    class Meta:
        model = Establecimiento
        exclude = ('register', 'representante', 'clasificacion', 'categoria',)


YEAR_CHOICES = map(str, range(datetime.now().year - 3, datetime.now().year + 3))


class EstablecimientoRegistroForm(forms.ModelForm):

    def __init__(self, id, *args, **kwargs):
        super(EstablecimientoRegistroForm, self).__init__(*args, **kwargs)
        self.fields['establecimiento'] = forms.ModelChoiceField(queryset=Establecimiento.objects.filter(id=id),
                                                                initial=id, widget=forms.HiddenInput())
        self.fields['fecha'] = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                               initial=datetime.now().date())

        self.fields['tipo_tarifa'] = forms.ModelChoiceField(queryset=Items.objects.filter(catalogo_id=4))

    class Meta:
        model = EstablecimientoRegistro
        exclude = ('register', 'estado', 'porcentaje_ocupacion', 'revpar')

    def clean(self):
        cleaned_data = super(EstablecimientoRegistroForm, self).clean()
        habitaciones_disponibles = cleaned_data.get('habitaciones_disponibles')
        habitaciones_ocupadas = cleaned_data.get('habitaciones_ocupadas')
        tarifa_promedio = cleaned_data.get('tarifa_promedio')

        if habitaciones_ocupadas > habitaciones_disponibles:
            self.add_error('habitaciones_ocupadas', 'No puede haber más habitaciones ocupadas que disponibles')

        if tarifa_promedio == 0:
            self.add_error('tarifa_promedio', 'La tarifa debería ser mayor a cero')

            # def clean_habitaciones_ocupadas(self):
    #     habitaciones_disponibles = self.cleaned_data.get('habitaciones_disponibles')
    #     habitaciones_ocupadas = self.cleaned_data.get('habitaciones_ocupadas')
    #     print habitaciones_disponibles, habitaciones_ocupadas
    #     if habitaciones_ocupadas > habitaciones_disponibles:
    #         print "error"
    #         raise forms.ValidationError(_("No puede haber más habitaciones ocupadas que disponibles"))
    #     return habitaciones_disponibles


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
    captcha = ReCaptchaField()