from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterAPIView(APIView):
    permission_classes = [IsAdminUser] #Obligar a que sólo los administradores puedan crear usuarios
    def post(self, request):
        print("Estamos en el register")
        register_serializer = UserSerializer(data=request.data)
        register_serializer.is_valid(raise_exception=True)
        register_serializer.save()
        return Response(register_serializer.data)

class LogoutAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Cierre de Sesión Exitoso!."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Error al Cerrar Sesión."}, status=status.HTTP_400_BAD_REQUEST)