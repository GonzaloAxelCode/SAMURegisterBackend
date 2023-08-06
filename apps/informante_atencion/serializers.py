from rest_framework import serializers
from .models import InformanteAtencion


class InformanteAtencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformanteAtencion
        fields = '__all__'
