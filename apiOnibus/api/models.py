from django.db import models

class rotas(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=512)

class onibus(models.Model):
    velocidade = models.FloatField()
    idRota = models.ForeignKey(rotas, on_delete=models.PROTECT)

class usuario(models.Model):
    permissao = models.IntegerField()
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=128)

class ultimalocalizacao(models.Model):
    idOnibus = models.ForeignKey(onibus, on_delete=models.PROTECT)
    data = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class rotasPontos(models.Model):
    idRota = models.ForeignKey(rotas, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()

class horarioRota(models.Model):
    idRota = models.ForeignKey(rotas, on_delete=models.PROTECT)
    inicio = models.CharField(max_length=5)
    fim = models.CharField(max_length=5)
    dias = models.CharField(max_length=7)

class ultimaLocalizacaoUsuario(models.Model):
    idUsuario = models.ForeignKey(usuario, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    


# Create your models here.
