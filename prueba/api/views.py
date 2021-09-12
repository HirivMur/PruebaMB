#from django.http import response
from django.shortcuts import render

from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.fields import JSONField
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import UsuarioSerializer
import json
from api.models import Usuario

class API_Usuario(APIView):
    def get(self, request):
        try:
            usuarios= Usuario.objects.all().values()
            serializers_usuarios= UsuarioSerializer(usuarios, many=True)
            return Response(serializers_usuarios.data)           
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request, format=None):
        try:
            serializer = UsuarioSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class API_delete_update(APIView):
    def delete(self,request,id,format=None):
        try:
            if Usuario.objects.filter(pk=id).exists():
                usuario = Usuario.objects.get(id=id)
                usuario.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response("INTERNAL_SERVER_ERROR",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, id, format=None):
        try:
            if Usuario.objects.filter(pk=id).exists():
                usuario = Usuario.objects.get(id=id)
                serializer = UsuarioSerializer(usuario, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response("INTERNAL_SERVER_ERROR",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Usuario_alfabetico(APIView):
    def get(self, request):
        try:
            lista_ordenada=[]
            usuarios= Usuario.objects.all()
            lista_usuarios=list(usuarios)
            aux=True
            while lista_usuarios:

                index=lista_usuarios[0]
                for usuario in lista_usuarios:
                    if usuario.apellido_paterno < index.apellido_paterno:
                        index = usuario
                lista_ordenada.append(index)
                lista_usuarios.remove(index)
            serializer=UsuarioSerializer(lista_ordenada,many=True).data
            return Response(serializer)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)   
            
class Usuario_edad(APIView):
    def get(self, request):
        try:
            lista_ordenada=[]
            usuarios= Usuario.objects.all()
            lista_usuarios=list(usuarios)
            aux=True
            while lista_usuarios:

                index=lista_usuarios[0]
                for usuario in lista_usuarios:
                    if usuario.edad < index.edad:
                        index = usuario
                lista_ordenada.append(index)
                lista_usuarios.remove(index)
            serializer=UsuarioSerializer(lista_ordenada,many=True).data
            return Response(serializer)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)