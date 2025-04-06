from rest_framework import viewsets
from django.db.models import Q
from django.db import models
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .models import PlanDescontaminacion, Organismo, TipoMedida, Medida, RegistroMedida
from .serializers import OrganismoSerializer, PlanDescontaminacionSerializer, MedidaSerializer, TipoMedidaSerializer, RegistroMedidaSerializer

class OrganismoViewSet(viewsets.ModelViewSet):
    queryset = Organismo.objects.all()
    serializer_class = OrganismoSerializer

    @action(detail=True, methods=['get'])
    def medidas_asignadas(self, request, pk=None):
        organismo = self.get_object()
        queryset = Medida.objects.filter(organismo=organismo)
        print(queryset)
        medidas = [medida.nombre for medida in queryset]
        return Response({'Organismo': organismo.nombre, 'Medidas': medidas})

class PlanDescontaminacionViewSet(viewsets.ModelViewSet):
    queryset = PlanDescontaminacion.objects.all()
    serializer_class = PlanDescontaminacionSerializer

class MedidaViewSet(viewsets.ModelViewSet):
    queryset = Medida.objects.all()
    serializer_class = MedidaSerializer

    @action(detail=False, methods=['get'])
    def estado_medidas(self, request):
        estado_medidas = {}

        for medida in Medida.objects.all():
            if medida.estado in estado_medidas.keys():
                estado_medidas[medida.estado].append(medida.nombre)
            else:
                estado_medidas[medida.estado] = [medida.nombre]

        return Response(estado_medidas)


class TipoMedidaViewSet(viewsets.ModelViewSet):
    queryset = TipoMedida.objects.all()
    serializer_class = TipoMedidaSerializer

    @action(detail=True, methods=['get'])
    def medidas_tipo(self, request, pk=None):
        tipo = self.get_object()
        queryset = Medida.objects.filter(tipo_medida=tipo).values('tipo_medida__nombre').annotate(total=models.Count('tipo_medida'))
        medidas = [medida for medida in queryset]

        return Response(medidas)


class RegistroMedidaViewSet(viewsets.ModelViewSet):
    queryset = RegistroMedida.objects.all()
    serializer_class = RegistroMedidaSerializer

