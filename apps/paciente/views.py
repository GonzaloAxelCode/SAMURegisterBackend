from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.utils import timezone

from apps.paciente.serializers import PacienteSerializer


from .models import Paciente

from core.utils import CustomPageNumberPagination


class PacienteView(generics.ListAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    pagination_class = CustomPageNumberPagination


class AgregarPacienteView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PacienteSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ActualizarPacienteView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, paciente_id):
        try:
            paciente = Paciente.objects.get(pk=paciente_id)
            serializer = PacienteSerializer(paciente, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Paciente.DoesNotExist:
            return Response("El paciente no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ActivarPacienteView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, paciente_id):
        try:
            paciente = Paciente.objects.get(pk=paciente_id)
            paciente.activate = True
            paciente.save()
            return Response("Paciente activado.", status=status.HTTP_200_OK)
        except Paciente.DoesNotExist:
            return Response("El paciente no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DesactivarPacienteView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, paciente_id):
        try:
            paciente = Paciente.objects.get(pk=paciente_id)
            paciente.activate = False
            paciente.save()
            return Response("Paciente desactivado.", status=status.HTTP_200_OK)
        except Paciente.DoesNotExist:
            return Response("El paciente no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
