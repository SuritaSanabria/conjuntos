from django.db import models
from django.contrib.auth.models import Group
from apps.usuarios.models import CustomUser


residentes, _ = Group.objects.get_or_create(name='Residentes')

# Create your models here.

class TipoDocumento(models.Model):
    detalle = models.CharField(max_length=45)
    def __str__(self):
        return str(self.detalle)
    
class Tarifas(models.Model):
    detalle = models.CharField(max_length=45)
    valor = models.DecimalField(max_digits=16, decimal_places=2)
    intmor = models.DecimalField(max_digits=4, decimal_places=2)
    imprevistos = models.DecimalField(max_digits=14, decimal_places=2)
    estados = models.CharField(max_length=2, choices=(('A','A'), ('I','I'), ('H','H')))
    
    def __str__(self):
        return str(self.valor)
    
    
class Cuotas_Extras(models.Model):
    detalle = models.CharField(max_length=45)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    estado = models.CharField(max_length=2, choices=(('A','A'),('I','I')))
    def __str__(self):
        return str(self.valor)
    
class Terceros(models.Model):
    tipDocumento = models.ForeignKey(to=TipoDocumento, on_delete=models.CASCADE)
    numDoc = models.CharField(max_length=45)
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    telmov = models.CharField(max_length=12)
    def __str__(self) -> str:
        return str(self.numDoc)
    
class Conceptos_Otros(models.Model):
    detalle = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    estado = models.CharField(max_length=2, choices=(('A', 'A'),('I','I')))
    def __str__(self) -> str:
        return str(self.detalle)
    
class Parametrización(models.Model):
    nit = models.CharField(max_length=15)
    razsoc = models.CharField(max_length=80)
    direccion = models.CharField(max_length=60)
    ciudad = models.CharField(max_length=60)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    plazo = models.IntegerField()
    imprevisto = models.DecimalField(max_digits=14, decimal_places=2)
    intmor = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.CharField(max_length=100)
    
class Conceptos_Gastos(models.Model):
    detalle = models.CharField(max_length=60)
    def __str__(self):
        return str(self.detalle)
    

class Inmuebles (models.Model):
    codigo = models.CharField(max_length=20)
    fecha = models.DateField()
    id_usuario = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
    
    
class Tar_Inm(models.Model):
    id_inmueble = models.ForeignKey(to=Inmuebles, on_delete=models.CASCADE)
    tarifa = models.ForeignKey(to=Tarifas, on_delete=models.CASCADE)
    usuario = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    fechainicio = models.DateField()
    fechafin = models.DateField()
    
    
class Ext_Inm(models.Model):
    inmueble = models.ForeignKey(to=Inmuebles, on_delete=models.CASCADE)
    cuota_extra = models.ForeignKey(to=Cuotas_Extras, on_delete=models.CASCADE)
    fecha = models.DateField()
    usuario = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    
class Inm_Ter(models.Model):
    inmueble = models.ForeignKey(to=Inmuebles, on_delete=models.CASCADE)
    tercero = models.ForeignKey(to=Terceros, on_delete=models.CASCADE)
    relacion = models.CharField(max_length=40)
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=2, choices=(('A', 'A'), ('I','I')))

    
class Otro_inm(models.Model):
    inmueble = models.ForeignKey(to=Inmuebles, on_delete=models.CASCADE)
    concepto = models.ForeignKey(to=Conceptos_Otros,on_delete=models.CASCADE)
    fecha = models.DateField()
    usuario = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

class Gastos(models.Model):
    fecha = models.DateField()
    usuario = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    concepto = models.ForeignKey(to= Conceptos_Gastos, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    nota = models.CharField(max_length=150)
    estado = models.CharField(max_length=2, choices=(('A','A'), ('C', 'C')))
    
class Facturas(models.Model):
    numero = models.CharField(max_length=7, unique=True)
    fecha = models.DateField()
    inmueble = models.ForeignKey(to=Inmuebles, on_delete=models.CASCADE)
    tercero = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=45)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    fechaPago = models.DateField()
    impresion=models.CharField(max_length=2, choices=(('S','S'), ('N','N')))
    
class Bancos(models.Model):
    detalle = models.CharField(max_length=45)
    codBanco = models.IntegerField(primary_key=True, unique=True, )
    def __str__(self) -> str:
        return str(self.detalle)
class CuentasBancarias(models.Model):
    numCue= models.CharField(max_length=20)
    banco = models.ForeignKey(Bancos, on_delete=models.CASCADE)
    tipoCue = models.CharField(max_length=2, choices=(('CC','CC'), ('CA', 'CA')))
    pago = models.CharField(max_length=2, choices=(('S', 'S'), ('N', 'N')))
    estado = models.CharField(max_length=2, choices=(('A', 'A'),('I', 'I')))
    def __str__(self) -> str:
        return str(self.numCue)
    
class Detalle_Gas(models.Model):
    secuencia = models.IntegerField(unique=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    pago = models.CharField(max_length=20)
    banco = models.ForeignKey(to=Bancos, on_delete=models.CASCADE)
    tipTar = models.CharField(max_length=2, choices=(('C', 'C'), ('D', 'D')))
    numaut=models.CharField(max_length=6)
    cuenta = models.ForeignKey(to=CuentasBancarias, on_delete=models.CASCADE)
    
    
class Recaudos(models.Model):
    fecha = models.DateField()
    usuario = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    Inmuebles=models.ForeignKey(to=Inmuebles, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=14,decimal_places=2)
    deuda = models.DecimalField(max_digits=14, decimal_places=2)
    documento = models.CharField(max_length=7)
    nota = models.CharField(max_length=150)
    estado = models.CharField(max_length=1, choices=(('E','E'),('P','P'),('C', 'C')))
    def __str__(self) -> str:
        return str(self.nota)
    
class Detalle_Rec(models.Model):
    recaudo = models.ForeignKey(to=Recaudos, on_delete=models.CASCADE)
    secuencia = models.IntegerField(unique=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    pago = models.CharField(max_length=40, choices=(('EF','EF'), ('CF', 'CF'), ('TA', 'TA'), ('OB', 'OB')))
    cuenta = models.ForeignKey(to=CuentasBancarias, on_delete=models.CASCADE)
    numero=models.CharField(max_length=20)
    banco = models.ForeignKey(to=Bancos, on_delete=models.CASCADE)
    tipTar = models.CharField(max_length=2, choices=(('CC', 'CC'), ('CD', 'CD')))
    numAuth = models.CharField(max_length=6)
    
class Novedades(models.Model):
    idInmueble = models.OneToOneField(to=Inmuebles, on_delete=models.CASCADE)
    fecha = models.DateField()
    usuario = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    detalles = models.CharField(max_length=150)
    estado = models.CharField(max_length=2,choices=(('P','P'), ('A', 'A')))
    def __str__(self) -> str:
        return str(self.detalles)
    
class notas_novedad(models.Model):
    novedad = models.OneToOneField(to=Novedades, on_delete=models.CASCADE)
    inmueble = models.ForeignKey(to=Inmuebles, on_delete=models.CASCADE)
    fecha = models.DateField()
    usuario = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    detalle = models.CharField(max_length=150)
    def __str__(self) -> str:
        return str(self.detalle)
    
    
class Multas(models.Model):
    inmueble = models.ForeignKey(to=Inmuebles, on_delete=models.CASCADE)
    fecha = models.DateField()
    usuario = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    

class Cartera(models.Model):
    marca = models.CharField(max_length=10, choices=(('AD', 'AD'), ('MU', 'MU'),
('CE', 'CE'), ('OT', 'OT'), ('PA', 'PA'),
('IN','PA')))
    documento = models.CharField(max_length=7)
    fecha = models.DateField()
    detalle = models.CharField(max_length=45)
    idInmueble = models.ForeignKey(to=Inmuebles, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    naturaleza = models.CharField(max_length=12,choices=(('D','D'), ('C', 'C')))
    docori = models.CharField(max_length=20)
    docru = models.CharField(max_length=10)
    marcru = models.CharField(max_length=45)
    estado =models.CharField(max_length=1, choices=(('A','A'),('P','P'), ('C', 'C')))

class Auditoria(models.Model):
    sec = models.IntegerField()
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.CharField(max_length=8)
    tipo = models.CharField(max_length=1, choices=(('I','I'),('U','U'),('D','D')
        ))
        