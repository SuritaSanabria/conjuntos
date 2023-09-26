from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import (TipoDocumento, Tarifas, Cuotas_Extras, Terceros, Conceptos_Otros,
                     Parametrización, Conceptos_Gastos, Inmuebles, Tar_Inm, Ext_Inm,
                     Inm_Ter, Otro_inm, Gastos, Facturas, Bancos, CuentasBancarias,
                     Detalle_Gas, Recaudos, Detalle_Rec, Novedades, notas_novedad,
                     Multas, Cartera, Auditoria)
from .forms import (
    TipoDocumentoForm, TarifasForm, Cuotas_Extras_Form, Terceros_Form,
    Conceptos_Otros_Form, ParametrizacionForm, Conceptos_Gastos_Form,
    InmueblesForm, Tar_InmForm, Ext_InmForm, Inm_TerForm, Otron_Im_Form,
    GastosForm, FacturasForm, BancosForm, CuentasBancariasForm,
    Detalle_GasForm, RecaudosForm, Detalle_recForm, NovedadesForm,
    NotasForm, MultasForm, CarteraForm, AuditoriaForm
)

from apps.usuarios.models import CustomUser


@login_required
def base_edit_view(request, tabla, formulario, objeto_id, template):
    elemento = tabla.objects.get(pk=objeto_id)
    
    if request.method == 'POST':
        form = formulario(request.POST, instance=elemento)
        if form.is_valid():
            form.save()
            return redirect(request.path_info)
    else:
        form = formulario(instance=elemento)
        
    return render(request, f'conjunto/{template}', {'form': form, 'elemento': elemento})


@login_required
def base_form_view(request, tabla, formulario, template):
    elemento = tabla.objects.all()
    form = formulario(request.POST) if request.method == 'POST' else formulario()
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = formulario()
        return redirect(request.path_info)        
        
    return render(request, f'conjunto/{template}', {'form': form, 'elementos': elemento})

def tipo_documento_form(request):
    return base_form_view(request, TipoDocumento, TipoDocumentoForm, 'tipo_documento_form.html')

def tarifas_form(request):
    return base_form_view(request, Tarifas, TarifasForm, 'tarifas_form.html')

def cuotas_extras_form(request):
    return base_form_view(request, Cuotas_Extras, Cuotas_Extras_Form, 'cuotas_extras_form.html')

def terceros_form(request):
    return base_form_view(request, Terceros, Terceros_Form, 'terceros_form.html')

def conceptos_otros_form(request):
    return base_form_view(request, Conceptos_Otros, Conceptos_Otros_Form, 'conceptos_otros_form.html')

def parametrizacion_form(request):
    return base_form_view(request, Parametrización, ParametrizacionForm, 'parametrizacion_form.html')

def conceptos_gastos_form(request):
    return base_form_view(request, Conceptos_Gastos, Conceptos_Gastos_Form, 'conceptos_gastos_form.html')

def inmuebles_form(request):
    return base_form_view(request, Inmuebles, InmueblesForm, 'inmuebles_form.html')

def tar_inm_form(request):
    return base_form_view(request, Tar_Inm, Tar_InmForm, 'tar_inm_form.html')

def ext_inm_form(request):
    return base_form_view(request, Ext_Inm, Ext_InmForm, 'ext_inm_form.html')

def inm_ter_form(request):
    return base_form_view(request, Inm_Ter, Inm_TerForm, 'inm_ter_form.html')

def otron_im_form(request):
    return base_form_view(request, Otro_inm, Otron_Im_Form, 'otron_im_form.html')

def gastos_form(request):
    return base_form_view(request, Gastos, GastosForm, 'gastos_form.html')

def facturas_form(request):
    return base_form_view(request, Facturas, FacturasForm, 'facturas_form.html')

def bancos_form(request):
    return base_form_view(request, Bancos, BancosForm, 'bancos_form.html')

def cuentas_bancarias_form(request):
    return base_form_view(request, CuentasBancarias, CuentasBancariasForm, 'cuentas_bancarias_form.html')

def detalle_gas_form(request):
    return base_form_view(request, Detalle_Gas, Detalle_GasForm, 'detalle_gas_form.html')

def recaudos_form(request):
    return base_form_view(request, Recaudos, RecaudosForm, 'recaudos_form.html')

def detalle_rec_form(request):
    return base_form_view(request, Detalle_Rec, Detalle_recForm, 'detalle_rec_form.html')

def novedades_form(request):
    return base_form_view(request, Novedades, NovedadesForm, 'novedades_form.html')

def notas_form(request):
    return base_form_view(request, notas_novedad, NotasForm, 'notas_form.html')

def multas_form(request):
    return base_form_view(request, Multas, MultasForm, 'multas_form.html')

def cartera_form(request):
    return base_form_view(request, Cartera, CarteraForm, 'cartera_form.html')

def auditoria_form(request):
    return base_form_view(request, Auditoria, AuditoriaForm, 'auditoria_form.html')

def tipo_documento_edit(request, objeto_id):
    return base_edit_view(request, TipoDocumento, TipoDocumentoForm, objeto_id, 'tipo_documento_form.html')

def tarifas_edit(request, objeto_id):
    return base_edit_view(request, Tarifas, TarifasForm, objeto_id, 'tarifas_form.html')

def cuotas_extras_edit(request, objeto_id):
    return base_edit_view(request, Cuotas_Extras, Cuotas_Extras_Form, objeto_id, 'cuotas_extras_form.html')

def terceros_edit(request, objeto_id):
    return base_edit_view(request, Terceros, Terceros_Form, objeto_id, 'terceros_form.html')

def conceptos_otros_edit(request, objeto_id):
    return base_edit_view(request, Conceptos_Otros, Conceptos_Otros_Form, objeto_id, 'conceptos_otros_form.html')

def parametrizacion_edit(request, objeto_id):
    return base_edit_view(request, Parametrización, ParametrizacionForm, objeto_id, 'parametrizacion_form.html')

def conceptos_gastos_edit(request, objeto_id):
    return base_edit_view(request, Conceptos_Gastos, Conceptos_Gastos_Form, objeto_id, 'conceptos_gastos_form.html')

def inmuebles_edit(request, objeto_id):
    return base_edit_view(request, Inmuebles, InmueblesForm, objeto_id, 'inmuebles_form.html')

def tar_inm_edit(request, objeto_id):
    return base_edit_view(request, Tar_Inm, Tar_InmForm, objeto_id, 'tar_inm_form.html')

def ext_inm_edit(request, objeto_id):
    return base_edit_view(request, Ext_Inm, Ext_InmForm, objeto_id, 'ext_inm_form.html')

def inm_ter_edit(request, objeto_id):
    return base_edit_view(request, Inm_Ter, Inm_TerForm, objeto_id, 'inm_ter_form.html')

def otron_im_edit(request, objeto_id):
    return base_edit_view(request, Otro_inm, Otron_Im_Form, objeto_id, 'otron_im_form.html')

def gastos_edit(request, objeto_id):
    return base_edit_view(request, Gastos, GastosForm, objeto_id, 'gastos_form.html')

def facturas_edit(request, objeto_id):
    return base_edit_view(request, Facturas, FacturasForm, objeto_id, 'facturas_form.html')

def bancos_edit(request, objeto_id):
    return base_edit_view(request, Bancos, BancosForm, objeto_id, 'bancos_form.html')

def cuentas_bancarias_edit(request, objeto_id):
    return base_edit_view(request, CuentasBancarias, CuentasBancariasForm, objeto_id, 'cuentas_bancarias_form.html')

def detalle_gas_edit(request, objeto_id):
    return base_edit_view(request, Detalle_Gas, Detalle_GasForm, objeto_id, 'detalle_gas_form.html')

def recaudos_edit(request, objeto_id):
    return base_edit_view(request, Recaudos, RecaudosForm, objeto_id, 'recaudos_form.html')

def detalle_rec_edit(request, objeto_id):
    return base_edit_view(request, Detalle_Rec, Detalle_recForm, objeto_id, 'detalle_rec_form.html')

def novedades_edit(request, objeto_id):
    return base_edit_view(request, Novedades, NovedadesForm, objeto_id, 'novedades_form.html')

def notas_edit(request, objeto_id):
    return base_edit_view(request, notas_novedad, NotasForm, objeto_id, 'notas_form.html')

def multas_edit(request, objeto_id):
    return base_edit_view(request, Multas, MultasForm, objeto_id, 'multas_form.html')

def cartera_edit(request, objeto_id):
    return base_edit_view(request, Cartera, CarteraForm, objeto_id, 'cartera_form.html')

def auditoria_edit(request, objeto_id):
    return base_edit_view(request, Auditoria, AuditoriaForm, objeto_id, 'auditoria_form.html')