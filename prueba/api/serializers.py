from api.models import Usuario
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido_materno', 'apellido_paterno', 'edad','email', 'telefono']