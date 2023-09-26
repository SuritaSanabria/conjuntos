from django.contrib import admin
from .models import (TipoDocumento, Tarifas, Cuotas_Extras, Terceros, Conceptos_Otros,
                     Parametrización, Conceptos_Gastos, Inmuebles, Tar_Inm, Ext_Inm,
                     Inm_Ter, Otro_inm, Gastos, Facturas, Bancos, CuentasBancarias,
                     Detalle_Gas, Recaudos, Detalle_Rec, Novedades, notas_novedad,
                     Multas, Cartera, Auditoria)

# Para registrar todos los modelos en una sola llamada
admin.site.register([
    TipoDocumento, Tarifas, Cuotas_Extras, Terceros, Conceptos_Otros,
    Parametrización, Conceptos_Gastos, Inmuebles, Tar_Inm, Ext_Inm,
    Inm_Ter, Otro_inm, Gastos, Facturas, Bancos, CuentasBancarias,
    Detalle_Gas, Recaudos, Detalle_Rec, Novedades, notas_novedad,
    Multas, Cartera, Auditoria
])
