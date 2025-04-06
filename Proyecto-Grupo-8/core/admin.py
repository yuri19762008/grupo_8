from django.contrib import admin
from .models import PlanDescontaminacion, Organismo, TipoMedida, Medida, RegistroMedida

@admin.register(Organismo)
class OrganismoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'descripcion', 'contacto')
    search_fields = ('id','nombre','descripcion')
    list_filter = ('id',)
    ordering = ('id',)

@admin.register(TipoMedida)
class TipoMedidaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'descripcion')
    search_fields = ('id','nombre')
    list_filter = ('id',)
    ordering = ('id',)

@admin.register(Medida)
class MedidaAdmin(admin.ModelAdmin):
    list_display = ('id','organismo', 'tipo_medida', 'nombre','indicador','formula_calculo','frecuencia_reporte','medio_verificacion','estado')
    search_fields = ('id','nombre','tipo_medida__nombre')
    list_filter = ('id','tipo_medida','estado')
    ordering = ('id',)

@admin.register(PlanDescontaminacion)
class PlanDescontaminacionAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','region','descripcion','fecha_inicio','fecha_fin','get_medidas')
    search_fields = ('id','nombre','region')
    list_filter = ('id','region')
    ordering = ('id',)

    def get_medidas(self, obj):
        return ", ".join([str(m.id) + ") "+m.nombre for m in obj.medidas.all()])
    get_medidas.short_description = 'Medidas'


admin.site.register(RegistroMedida)


