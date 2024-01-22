import base64
from rest_framework.views import APIView
from rest_framework import status
import requests
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model

from .serializers import UserProfileSerializer

# Create your views here.
class ExternalResourceAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        # URL del recurso externo que deseas consumir
        external_resource_url = 'https://sandbox.belvo.com/api/institutions/?page=1'

        try:
            # Realizar una solicitud GET al recurso externo
            id_belvo = 'd1966748-8844-4999-b904-2cce4d4475af'
            pass_belvo = '0n-ITcGZ1CSCjTtL0qcvwXqOyHrcBgqx2B*-J648M6d81nLABp0rFO1mRKlTh-Ga'

            # Construir el encabezado de autenticación Basic Auth
            token = base64.b64encode(bytes(f'{id_belvo}:{pass_belvo}', 'utf-8'))
            print(str(token))
            headers = {
                'Authorization': bytes('Basic ', 'utf-8') + token  # Codificar a Base64
            }
            response = requests.get(external_resource_url, headers=headers)

            # Verificar si la solicitud fue exitosa (código 200)
            if response.status_code == 200:
                # Procesar los datos recibidos según tus necesidades
                data = response.json()
                # Puedes realizar operaciones con 'data' aquí

                # Devolver una respuesta con los datos procesados
                return Response(data, status=status.HTTP_200_OK)
            else:
                # Devolver una respuesta en caso de error en la solicitud externa
                print(response.text)
                return Response({'error': 'Error en la solicitud externa'}, status=response.status_code)

        except requests.exceptions.RequestException as e:
            # Capturar excepciones de solicitudes HTTP (por ejemplo, timeout, conexión rechazada, etc.)
            return Response({'error': f'Error de solicitud: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Logout exitoso'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'detail': 'Error al hacer logout'}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_data = UserProfileSerializer(request.user).data

        return Response(user_data, status=status.HTTP_200_OK)


from .serializers import UserCreateSerializer


class CreateUserView(CreateAPIView):

    model = get_user_model()
    serializer_class = UserCreateSerializer
