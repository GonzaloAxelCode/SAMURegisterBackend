from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.informante_atencion.serializers import InformanteAtencionSerializer
from apps.personal_medico.models import PersonalMedico


from .models import InformanteAtencion

from core.utils import CustomPageNumberPagination


class InformanteAtencionView(generics.ListAPIView):
    queryset = InformanteAtencion.objects.all()
    serializer_class = InformanteAtencionSerializer
    pagination_class = CustomPageNumberPagination


class AgregarInformanteAtencionView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = InformanteAtencionSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ActualizarInformanteAtencionView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, informante_id):
        try:
            informante_atencion = InformanteAtencion.objects.get(
                pk=informante_id)
            serializer = InformanteAtencionSerializer(
                informante_atencion, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except InformanteAtencion.DoesNotExist:
            return Response("El Informante no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ActivarInformanteAtencionView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, informante_id):
        try:
            informante_atencion = InformanteAtencion.objects.get(
                pk=informante_id)

            informante_atencion.activate = True
            informante_atencion.save()
            return Response("Informante activado.", status=status.HTTP_200_OK)
        except InformanteAtencion.DoesNotExist:
            return Response("El Informante no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DesactivarInformanteAtencion(APIView):
    permission_classes = [AllowAny]

    def post(self, request, informante_id):
        try:
            informante_atencion = InformanteAtencion.objects.get(
                pk=informante_id)
            informante_atencion.activate = False
            informante_atencion.save()
            return Response("Informante desactivado.", status=status.HTTP_200_OK)
        except InformanteAtencion.DoesNotExist:
            return Response("El Informante no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
