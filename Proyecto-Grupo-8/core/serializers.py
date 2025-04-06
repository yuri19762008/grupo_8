from rest_framework import serializers
from .models import Organismo, PlanDescontaminacion, Medida, TipoMedida, RegistroMedida

class OrganismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organismo
        fields = '__all__'

class PlanDescontaminacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanDescontaminacion
        fields = '__all__'

class MedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medida
        fields = '__all__'

class TipoMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMedida
        fields = '__all__'

class RegistroMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroMedida
        fields = '__all__'
