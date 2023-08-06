from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Diagnostico
from .serializers import DiagnosticoSerializer
from core.utils import CustomPageNumberPagination


class DiagnosticoView(generics.ListAPIView):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer
    pagination_class = CustomPageNumberPagination


class AgregarDiagnosticoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = DiagnosticoSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ActualizarDiagnosticoView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, diagnostico_id):
        try:
            diagnostico = Diagnostico.objects.get(pk=diagnostico_id)
            serializer = DiagnosticoSerializer(
                diagnostico, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Diagnostico.DoesNotExist:
            return Response("El El Diagnostico no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ActivarDiagnosticoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, diagnostico_id):
        try:
            diagnostico = Diagnostico.objects.get(pk=diagnostico_id)
            diagnostico.activate = True
            diagnostico.save()
            return Response("El Diagnostico activado.", status=status.HTTP_200_OK)
        except Diagnostico.DoesNotExist:
            return Response("El El Diagnostico no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DesactivarDiagnosticoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, diagnostico_id):
        try:
            diagnostico = Diagnostico.objects.get(pk=diagnostico_id)
            diagnostico.activate = False
            diagnostico.save()
            return Response("El Diagnostico desactivado.", status=status.HTTP_200_OK)
        except Diagnostico.DoesNotExist:
            return Response("El El Diagnostico no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
