from django import forms
from .models import (TipoDocumento, Tarifas, Cuotas_Extras, Terceros, Conceptos_Otros,
                     Parametrización, Conceptos_Gastos, Inmuebles, Tar_Inm, Ext_Inm,
                     Inm_Ter, Otro_inm, Gastos, Facturas, Bancos, CuentasBancarias,
                     Detalle_Gas, Recaudos, Detalle_Rec, Novedades, notas_novedad,
                     Multas, Cartera, Auditoria)

def create_model_form(model_class):
    class DynamicModelForm(forms.ModelForm):
        class Meta:
            model = model_class
            fields = '__all__'
    return DynamicModelForm

# Define los modelos y crea las clases de formulario
AuditoriaForm = create_model_form(Auditoria)
CarteraForm = create_model_form(Cartera)
MultasForm = create_model_form(Multas)
NotasForm = create_model_form(notas_novedad)
NovedadesForm = create_model_form(Novedades)
Detalle_recForm = create_model_form(Detalle_Rec)
RecaudosForm = create_model_form(Recaudos)
Detalle_GasForm = create_model_form(Detalle_Gas)
CuentasBancariasForm = create_model_form(CuentasBancarias)
BancosForm = create_model_form(Bancos)
FacturasForm = create_model_form(Facturas)
GastosForm = create_model_form(Gastos)
Otron_Im_Form = create_model_form(Otro_inm)
Inm_TerForm = create_model_form(Inm_Ter)
Ext_InmForm = create_model_form(Ext_Inm)
Tar_InmForm = create_model_form(Tar_Inm)
InmueblesForm = create_model_form(Inmuebles)
ParametrizacionForm = create_model_form(Parametrización)
Conceptos_Gastos_Form = create_model_form(Conceptos_Gastos)
TipoDocumentoForm = create_model_form(TipoDocumento)
TarifasForm = create_model_form(Tarifas)
Cuotas_Extras_Form = create_model_form(Cuotas_Extras)
Terceros_Form = create_model_form(Terceros)
Conceptos_Otros_Form = create_model_form(Conceptos_Otros)