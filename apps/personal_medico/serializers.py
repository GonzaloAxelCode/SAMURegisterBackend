

from rest_framework import serializers

from apps.personal_medico.models import PersonalMedico


class PersonalMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalMedico
        fields = '__all__'
