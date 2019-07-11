from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


class UltimaLocalizacao(APIView):
    def post(self, request):
        try:
            serializer = ultimalocalizacao(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_RESQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self, request):
        try:
            local = ultimalocalizacao.objects.all()
            serializer = ultimaLocalizacaoUsuarioSerializer(local, many=True)
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
     status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UltimaLocalizacaoDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == '0':
                return JsonResponse({'mensagem': "O id deve ser maior que zero"},
                                    status=status.HTTP_400_BAD_REQUEST)
            local = ultimalocalizacao.objects.get(pk=pk)
            serializer = ultimaLocalizaoSerializer(local)
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem':"Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self, request, pk):
        try:
            if pk == 0:
                return  JsonResponse({'mensagem': "O id deve ser maior que zero"},
                                    status=status.HTTP_400_BAD_REQUEST)
            local =ultimalocalizacao.objects.get(pk=pk)
            serializer = ultimaLocalizaoSerializer(local, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class HorarioRota(APIView):
    def get(self, request):
        try:
            lista_horario = horarioRota.objects.all()
            serializer = horarioRotaSerializer(lista_horario, many=True)
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
     status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class HorarioRotaDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == '0':
                return JsonResponse({'mensagem': "O id deve ser maior que zero"},
                                    status=status.HTTP_400_BAD_REQUEST)
            horario = horarioRota.objects.get(pk=pk)
            serializer = horarioRotaSerializer(horario, data=request.data)
            return Response(serializer.data)
        except horarioRota.DoesNotExist:
            return JsonResponse({'mensagem': "O horário não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem':"Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Usuario(APIView):
    def post(self, request):
        try:
            serializer = usuario(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_RESQUEST)
        except Exception:
            return JsonResponse({'mensagem':"Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self, request):
        try:
            user = usuario.objects.all()
            serializer = usuarioSerializer(user, many=True)
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
     status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UsuarioDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == '0':
                return JsonResponse({'mensagem': "O id deve ser maior que zero"},
                                    status=status.HTTP_400_BAD_REQUEST)
            user = usuario.objects.get(pk=pk)
            serializer = usuarioSerializer(user, data=request.data)
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem':"Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UltimaLocalizacaoUsuario(APIView):
    def post(self, request):
        try:
            serializer = ultimaLocalizacaoUsuario(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_RESQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UltimaLocalizacaoUsuarioDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == '0':
                return JsonResponse({'mensagem': "O id deve ser maior que zero"},
                                    status=status.HTTP_400_BAD_REQUEST)
            local = ultimaLocalizacaoUsuario.objects.get(pk=pk)
            serializer = ultimaLocalizacaoUsuarioSerializer(local)
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem':"Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self, request, pk):
        try:
            if pk == '0':
                return JsonResponse({'mensagem': "O id deve ser maior que zero"},
                                    status=status.HTTP_400_BAD_REQUEST)
            local =ultimaLocalizacaoUsuario.objects.get(pk=pk)
            serializer = ultimaLocalizacaoUsuarioSerializer(local, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Create your views here.
