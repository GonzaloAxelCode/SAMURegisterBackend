from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonalMedicoSerializer
from .models import PersonalMedico
from core.utils import CustomPageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework import generics, status


class PersonalMedicoView(generics.ListAPIView):
    queryset = PersonalMedico.objects.all()
    serializer_class = PersonalMedicoSerializer
    pagination_class = CustomPageNumberPagination


class AgregarPersonalMedicoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PersonalMedicoSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ActualizarPersonalMedicoView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, id_personal):
        try:
            personal = PersonalMedico.objects.get(pk=id_personal)
            serializer = PersonalMedicoSerializer(personal, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PersonalMedico.DoesNotExist:
            return Response("El personal médico no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ActivarPersonalMedicoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, id_personal):
        try:
            personal = PersonalMedico.objects.get(pk=id_personal)
            personal.activate = True
            personal.save()
            return Response("Personal médico activado.", status=status.HTTP_200_OK)
        except PersonalMedico.DoesNotExist:
            return Response("El personal médico no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DesactivarPersonalMedicoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, id_personal):
        try:
            personal = PersonalMedico.objects.get(pk=id_personal)
            personal.activate = False
            personal.save()
            return Response("Personal médico desactivado.", status=status.HTTP_200_OK)
        except PersonalMedico.DoesNotExist:
            return Response("El personal médico no existe.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
