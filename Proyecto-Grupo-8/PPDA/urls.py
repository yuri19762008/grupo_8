
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions #TODO: Revisar lógica de permisos para este proyecto
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from core.views import OrganismoViewSet, PlanDescontaminacionViewSet, TipoMedidaViewSet, MedidaViewSet, RegistroMedidaViewSet

router = DefaultRouter() #Exije que las vistas sean ViewSets : ModelViewsets, ViewSets
# router.register('token', LoginViewSet, basename='login') # LoginView no es un ViewSets
router.register('plan_descontaminacion', PlanDescontaminacionViewSet)
router.register('organismo', OrganismoViewSet)
router.register('tipo_medida', TipoMedidaViewSet)
router.register('medida', MedidaViewSet)
router.register('registro_medida', RegistroMedidaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/authentication/', include('authentication.urls')),

    # Documentación 
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
