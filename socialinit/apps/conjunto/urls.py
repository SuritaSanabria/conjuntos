from django.urls import path
from . import views

urlpatterns = [
    path('tipo_documento/', views.tipo_documento_form, name='tipo_documento_create'),
    path('tipo_documento/edit/<int:objeto_id>/', views.tipo_documento_edit, name='tipo_documento_edit'),
    
    path('tarifas/', views.tarifas_form, name='tarifas_create'),
    path('tarifas/edit/<int:objeto_id>/', views.tarifas_edit, name='tarifas_edit'),
    
    path('cuotas_extras/', views.cuotas_extras_form, name='cuotas_extras_create'),
    path('cuotas_extras/edit/<int:objeto_id>/', views.cuotas_extras_edit, name='cuotas_extras_edit'),
    
    path('terceros/', views.terceros_form, name='terceros_create'),
    path('terceros/edit/<int:objeto_id>/', views.terceros_edit, name='terceros_edit'),
    
    path('conceptos_otros/', views.conceptos_otros_form, name='conceptos_otros_create'),
    path('conceptos_otros/edit/<int:objeto_id>/', views.conceptos_otros_edit, name='conceptos_otros_edit'),
    
    path('parametrizacion/', views.parametrizacion_form, name='parametrizacion_create'),
    path('parametrizacion/edit/<int:objeto_id>/', views.parametrizacion_edit, name='parametrizacion_edit'),
    
    path('conceptos_gastos/', views.conceptos_gastos_form, name='conceptos_gastos_create'),
    path('conceptos_gastos/edit/<int:objeto_id>/', views.conceptos_gastos_edit, name='conceptos_gastos_edit'),
    
    path('inmuebles/', views.inmuebles_form, name='inmuebles_create'),
    path('inmuebles/edit/<int:objeto_id>/', views.inmuebles_edit, name='inmuebles_edit'),
    
    path('tar_inm/', views.tar_inm_form, name='tar_inm_create'),
    path('tar_inm/edit/<int:objeto_id>/', views.tar_inm_edit, name='tar_inm_edit'),
    
    path('ext_inm/', views.ext_inm_form, name='ext_inm_create'),
    path('ext_inm/edit/<int:objeto_id>/', views.ext_inm_edit, name='ext_inm_edit'),
    
    path('inm_ter/', views.inm_ter_form, name='inm_ter_create'),
    path('inm_ter/edit/<int:objeto_id>/', views.inm_ter_edit, name='inm_ter_edit'),
    
    path('otro_inm/', views.otron_im_form, name='otron_im_create'),
    path('otron_inm/edit/<int:objeto_id>/', views.otron_im_edit, name='otron_im_edit'),
    
    path('gastos/', views.gastos_form, name='gastos_create'),
    path('gastos/edit/<int:objeto_id>/', views.gastos_edit, name='gastos_edit'),
    
    path('facturas/', views.facturas_form, name='facturas_create'),
    path('facturas/edit/<int:objeto_id>/', views.facturas_edit, name='facturas_edit'),
    
    path('bancos/', views.bancos_form, name='bancos_create'),
    path('bancos/edit/<int:objeto_id>/', views.bancos_edit, name='bancos_edit'),
    
    path('cuentas_bancarias/', views.cuentas_bancarias_form, name='cuentas_bancarias_create'),
    path('cuentas_bancarias/edit/<int:objeto_id>/', views.cuentas_bancarias_edit, name='cuentas_bancarias_edit'),
    
    path('detalle_gas/', views.detalle_gas_form, name='detalle_gas_create'),
    path('detalle_gas/edit/<int:objeto_id>/', views.detalle_gas_edit, name='detalle_gas_edit'),
    
    path('recaudos/', views.recaudos_form, name='recaudos_create'),
    path('recaudos/edit/<int:objeto_id>/', views.recaudos_edit, name='recaudos_edit'),
    
    path('detalle_rec/', views.detalle_rec_form, name='detalle_rec_create'),
    path('detalle_rec/edit/<int:objeto_id>/', views.detalle_rec_edit, name='detalle_rec_edit'),
    
    path('novedades/', views.novedades_form, name='novedades_create'),
    path('novedades/edit/<int:objeto_id>/', views.novedades_edit, name='novedades_edit'),
    
    path('notas/', views.notas_form, name='notas_create'),
    path('notas/edit/<int:objeto_id>/', views.notas_edit, name='notas_edit'),
    
    path('multas/', views.multas_form, name='multas_create'),
    path('multas/edit/<int:objeto_id>/', views.multas_edit, name='multas_edit'),
    
    path('cartera/', views.cartera_form, name='cartera_create'),
    path('cartera/edit/<int:objeto_id>/', views.cartera_edit, name='cartera_edit'),
    
    path('auditoria/', views.auditoria_form, name='auditoria_create'),
    path('auditoria/edit/<int:objeto_id>/', views.auditoria_edit, name='auditoria_edit'),
]
