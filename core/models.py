from django.db import models
from django.contrib.auth.models import User


class Catalogo(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, blank=True)
    register = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'catalog'

    def __str__(self):
        return self.nombre


class Items(models.Model):
    nombre = models.CharField(max_length=255)
    catalogo = models.ForeignKey(Catalogo, db_column='catalogo', related_name='items', blank=True, null=True,
                                 on_delete=models.SET_NULL)
    descripcion = models.CharField(max_length=255, blank=True)
    register = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'items'
        verbose_name_plural = "Items"

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return self.nombre


class Canton(models.Model):
    nombre = models.CharField(max_length=255)
    provincia = models.ForeignKey(Provincia, db_column='provincia', related_name='cantones', on_delete=models.CASCADE)

    class Meta:
        db_table = 'canton'
        verbose_name_plural = 'Cantones'

    def __str__(self):
        return self.nombre


class Parroquia(models.Model):
    nombre = models.CharField(max_length=255)
    canton = models.ForeignKey(Canton, db_column='canton', related_name='parroquias', on_delete=models.CASCADE)

    class Meta:
        db_table = 'parroquia'
        verbose_name_plural = 'Parroquias'

    def __str__(self):
        return self.nombre


class UserProvincia(models.Model):
    user = models.ForeignKey(User, related_name="user_provincia", on_delete=models.CASCADE)
    provincias = models.ManyToManyField(Provincia)

    class Meta:
        db_table = "user_provincia"
        verbose_name_plural = 'Usuario Provincias'

    def __str__(self):
        return self.user.username


class Establecimiento(models.Model):
    registro_SIIT = models.CharField(max_length=255, blank=True)
    registro_SIETE = models.CharField(max_length=255, blank=True)
    nombre = models.CharField(max_length=255, help_text='Nombre del establecimiento')
    RUC = models.CharField(max_length=13, help_text='RUC del establecimiento')
    email = models.EmailField(max_length=255)
    web = models.URLField(max_length=255, blank=True)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=255)
    calle_principal = models.CharField(max_length=255, blank=True)
    calle_numero = models.CharField(max_length=10, blank=True)
    calle_secundaria = models.CharField(max_length=255, blank=True)
    # tipo = models.ForeignKey(Items,db_column='tipo',related_name='est_tipo',blank=True,null=True,on_delete=models.SET_NULL)
    clasificacion = models.ForeignKey(Items, db_column='clasificacion', related_name='est_clasificacion', blank=True,
                                      null=True, on_delete=models.SET_NULL)
    categoria = models.ForeignKey(Items, db_column='categoria', related_name='est_cat', blank=True, null=True,
                                  on_delete=models.SET_NULL)
    empleados = models.IntegerField(default=0)
    hombres = models.IntegerField(default=0)
    mujeres = models.IntegerField(default=0)
    discapacitados = models.IntegerField(default=0)
    empleados_habitaciones = models.IntegerField(default=0, help_text='Número de empleados para las habitaciones')
    empleados_alimentos_bebidas = models.IntegerField(default=0,
                                                      help_text='Número de empleados para atención de alimentos y bebidas')
    empleados_administrativos = models.IntegerField(default=0, help_text='Número de empleados administrativos')
    empleados_otras_areas = models.IntegerField(default=0,
                                                help_text='Número de empleados en otras áreas del establecimiento')
    local = models.CharField(max_length=255, null=True,
                             choices=(('arrendado', 'Arrendado'), ('propio', 'Propio'), ('cedido', 'Cedido'),))
    area_total = models.IntegerField(default=0, help_text='Metros cuadrados del establecimiento')
    area_alimentos_bebidas = models.IntegerField(default=0,
                                                 help_text='Metros cuadrados para el área de alimentos y bebidas')
    provincia = models.ForeignKey(Provincia, db_column='provincia', related_name='est_provincias', blank=True,
                                  null=True, on_delete=models.SET_NULL)
    canton = models.ForeignKey(Canton, db_column='canton', related_name='est_cantones', blank=True, null=True,
                               on_delete=models.SET_NULL)
    parroquia = models.ForeignKey(Parroquia, db_column='parroquia', related_name='est_parroquias', blank=True,
                                  null=True, on_delete=models.SET_NULL)
    habitaciones = models.IntegerField(default=0)
    plazas = models.IntegerField(default=0)
    propietario = models.CharField(max_length=255)
    representante = models.CharField(max_length=255, blank=True, null=True)
    latitud = models.CharField(max_length=255, blank=True, null=True)
    longitud = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, db_column='user', related_name='users', blank=True, null=True,
                             on_delete=models.SET_NULL)
    register = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'establecimiento'
        verbose_name = "Establecimiento"
        verbose_name_plural = "Establecimientos"

    def __str__(self):
        return self.nombre

    def get_ultimo_registro(self):
        return self.registros.latest('fecha')


class EstablecimientoRegistro(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, db_column='establecimiento', related_name='registros', on_delete=models.CASCADE)
    fecha = models.DateField()
    checkins = models.IntegerField(default=0, help_text=u'Número total de personas que registraron su ENTRADA')
    checkouts = models.IntegerField(default=0, help_text='Número total de personas que registraron su SALIDA')
    pernoctaciones = models.IntegerField(default=0,
                                         help_text='Número total de huéspedes que pernoctaron en el establecimiento')
    nacionales = models.IntegerField(default=0,
                                     help_text='Número total de huéspedes ECUATORIANOS que se registraron en el establecimiento')
    extranjeros = models.IntegerField(default=0,
                                      help_text='Número total de huéspedes EXTRANJEROS que se registraron en el establecimiento')
    habitaciones_ocupadas = models.IntegerField(default=0,
                                                help_text='Habitaciones vendidas o que estuvieron ocupadas este día')
    habitaciones_disponibles = models.IntegerField(default=0,
                                                   help_text='Habitaciones disponibles o habilitadas en el establecimiento, no incluye habitaciones en mantenimiento ni para uso del personal')
    tipo_tarifa = models.ForeignKey(Items, db_column='tipo_tarifa', related_name='est_tipo_tarfia', blank=True,
                                    null=True, on_delete=models.SET_NULL)
    tarifa_promedio = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                          help_text='Tarifa estándar o promedio aproximado de las tarifas cobradas durante el día')
    ventas_netas = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                       help_text='Únicamente ventas relacionadas con alojamiento, no incluye ventas de restaurantes, eventos, alquiler de auditorios, etc. No debe incluir impuestos ni tasas')
    porcentaje_ocupacion = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    revpar = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    empleados_temporales = models.IntegerField(default=0, help_text='Empleados contratados para este día')
    estado = models.CharField(max_length=15, default='sin_validar',
                              choices=(('sin_validar', 'sin_validar'), ('validado', 'validado'),))
    register = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'establecimiento_registro'
        verbose_name = "Registros de Establecimiento"
        verbose_name_plural = "Registros de Establecimiento"
        ordering = ['-fecha']

    def __str__(self):
        return u'{establecimiento} - checkins: {checkins} - checkouts: {checkouts}'.format(
            establecimiento=self.establecimiento, checkins=self.checkins, checkouts=self.checkouts)


# end file models.py
# Create your models here.
