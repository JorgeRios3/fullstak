from django.contrib.auth.models import User
from .models import Persona, Pago, Viaje
from rest_framework import serializers


class PagoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pago
        fields = ['fecha', 'total', 'persona']


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    #pagos = serializers.StringRelatedField(many=True)
    pagos = PagoSerializer(many=True)
    class Meta:
        model = Persona
        fields = ['nombre', 'edad', 'id', 'apellido_paterno', 'apellido_materno', 'pagos']
