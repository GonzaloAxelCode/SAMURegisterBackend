
from core.permissions import CustomPermission
from .serializers import UserAccountSerializer
from .models import UserAccount
from rest_framework.permissions import IsAdminUser
from django.conf import settings
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from django.db import transaction
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import authentication_classes
from google.oauth2 import id_token as google_id_token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from google.auth.transport import requests
from apps.user.models import Profile, Settings, UserAccount
from django.contrib.auth import get_user_model
User = get_user_model()


@authentication_classes([])
@permission_classes([AllowAny])
class GoogleLoginView(APIView):
    def post(self, request):
        id_token = request.data.get('id_token')
        if id_token:
            try:
                # Verificar el token de ID de Google y obtener la información de usuario

                info = google_id_token.verify_oauth2_token(
                    id_token, requests.Request(), settings.GOOGLE_CLIENT_ID)

                user = User.objects.filter(email=info['email']).first()

                if not user:
                    # Si no se encuentra un usuario con el correo electrónico de Google, crear uno nuevo

                    user = UserAccount(
                        email=info['email'], nickname=info['given_name'])
                    user.is_registered_with_google = True
                    user.nickname = info['given_name'] + "."
                    user.is_active = True
                    user.photo_url = info['picture']

                    user.first_name = info['given_name']

                    user.save()
                    # crear el objeto de perfil usuario
                    with transaction.atomic():
                        Profile.objects.create(user=user)
                        Settings.objects.create(user=user)
                    user.save()

                    refresh = RefreshToken.for_user(user)
                    access = refresh.access_token
                    return Response({
                        'access': str(access),
                        'refresh': str(refresh),
                        'is_new_account': True,

                    }, status=status.HTTP_200_OK)

                if user.is_registered_with_google:

                    refresh = RefreshToken.for_user(user)
                    access = refresh.access_token

                    return Response({
                        'access': str(access),
                        'refresh': str(refresh),

                    }, status=status.HTTP_200_OK)

                else:

                    return Response({"error": "El email esta asociado con una contraseña."}, status=status.HTTP_400_BAD_REQUEST)

            except ValueError:
                # Si no se puede verificar el token de ID de Google, retornar error
                return Response({'error': 'Invalid ID token'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'ID token not provided'}, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserView(APIView):
    permission_classes = [AllowAny, IsAdminUser]

    def delete(self, request):

        OutstandingToken.objects.all().delete()
        UserAccount.objects.all().delete()

        return Response({"mensaje": "Todos los usuarios eliminados"}, status=204)


class UserAccountListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        try:
            users = User.objects.exclude(nickname="Admin")
            serializer = UserAccountSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class UserAccountDeactivatePermissionView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            user.desactivate_account = True
            user.save()
            return Response({'message': 'Se le denego el permiso'}, status=status.HTTP_204_NO_CONTENT)

        except UserAccount.DoesNotExist:
            return Response({'error': 'No se encontró ningún usuario con ese correo electrónico.'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class UserAccountReactivatePermissionView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            user.desactivate_account = False
            user.save()
            return Response({'message': 'Se le otorgo el permiso'}, status=status.HTTP_204_NO_CONTENT)
        except UserAccount.DoesNotExist:
            return Response({'error': 'No se encontró ningún usuario con ese correo electrónico.'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
