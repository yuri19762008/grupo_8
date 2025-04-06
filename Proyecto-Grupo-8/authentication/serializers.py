from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'first_name', 
            'email', 
            'password', 
            'profile_type', 
        ]

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)  # Obtén el token y el refresh token
        user = self.user

        # Agrega información adicional del usuario al token
        data.update({
            "user_id": user.id,
            "email": user.email,  # Puedes agregar otros campos si es necesario
            "full_name": user.get_full_name(),  # Si tienes métodos personalizados en el modelo User
        })

        return data