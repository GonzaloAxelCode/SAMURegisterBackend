from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from apps.medico.models import Medico
from apps.medico.serializers import MedicoSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MedicoSerializer
from .models import Medico
from core.utils import CustomPageNumberPagination
from rest_framework.permissions import AllowAny


class MedicoView(generics.ListAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    pagination_class = CustomPageNumberPagination


class AgregarMedicoView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = MedicoSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ActualizarMedicoView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, id_medico):
        try:
            medico = Medico.objects.get(pk=id_medico)
            serializer = MedicoSerializer(medico, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Medico.DoesNotExist:
            return Response("El médico no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ActivarMedicoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, id_medico):
        try:
            medico = Medico.objects.get(pk=id_medico)
            medico.activate = True
            medico.save()
            return Response("Médico activado.", status=status.HTTP_200_OK)
        except Medico.DoesNotExist:
            return Response("El médico no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DesactivarMedicoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, id_medico):
        try:
            medico = Medico.objects.get(pk=id_medico)
            medico.activate = False
            medico.save()
            return Response("Médico desactivado.", status=status.HTTP_200_OK)
        except Medico.DoesNotExist:
            return Response("El médico no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
