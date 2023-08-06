

from rest_framework import serializers
from apps.atencion.models import Atencion


class AtencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atencion
        fields = '__all__'
