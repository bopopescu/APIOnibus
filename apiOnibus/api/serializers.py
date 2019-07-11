from rest_framework import serializers
from .models import *

class rotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = rotas
        fields = ["id", "nome", "descricao"]

class onibusSerializer(serializers.ModelSerializer):
    class Meta:
        model = onibus
        fields = ["id", "velocidade", "idRota"]

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ["id", "permissao", "nome", "email"] #verificar se precisa incluir a senha

class ultimaLocalizaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ultimalocalizacao
        fields = ["id", "idOnibus", "data", "latitude", "longitude"]

class rotasPontosSerializer(serializers.ModelSerializer):
    class Meta:
        model = rotasPontos
        fields = ["idRota", "latitude", "longitude"]

class horarioRotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = horarioRota
        fields = ["idRota", "inicio", "fim", "dias"]

class ultimaLocalizacaoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ultimaLocalizacaoUsuario
        fields = ["idUsuario", "latitude", "longitude"]