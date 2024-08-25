from ctypes.wintypes import SERVICE_STATUS_HANDLE
from sqlite3 import SQLITE_AUTH_USER
from telnetlib import STATUS
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import get_characters
from rest_framework import generics
from .models import Characters
import json

import requests
from rest_framework import viewsets
from rest_framework.response import Response


############# Aqui eu criei uma classe chamada RickandMorty e herdei a minha .viewset, após isso criei uma função que lista os parametros self e request e após isso criei uma váriavel chamada url onde está armazenada a API

class RickAndMortyViewSet(viewsets.ViewSet):
    def list(self, request):
        
        url = "https://rickandmortyapi.com/api/character/"
        
     
        response = requests.get(url)  ############ Usei aqui o método get para trazer a minha url fazendo uma resquicição http utilizando o ''requests'' que instalei usando o pip install requests
        
       
        if response.status_code == 200: ### Se o codigo de status for verdadeiro a váriavel data junto com o response.json me retornara o code 200
            data = response.json()
            return Response(data)
        else: ##### Se não retornar verdadeiro ocasionará o erro que não foi possivel exibir os dados 
            return Response({'error': 'Unable to fetch data'}, status=response.status_code)
        

    def retrieve(self, request, pk=None): ######### Nesta API que eu consumi não foi possivel realizar os métodos Create,Delete,Update
        url = f"https://rickandmortyapi.com/api/character/{pk}/"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()          
            return Response(data)
        else:
             return Response({'error': 'Character not found'}, status=response.status_code)
        
    def create(self, request): ######### Tentei realizer um método create mas a API nao permite

        return Response({'error': 'Create operation is not supported for external APIs'}, status=SERVICE_STATUS_HANDLE.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None): ####### A api não permite o método Update

        return Response({'error': 'Update operation is not supported for external APIs'}, status=STATUS.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None): ######## A api não permite o método Delete

        return Response({'error': 'Delete operation is not supported for external APIs'}, status=SQLITE_AUTH_USER.HTTP_405_METHOD_NOT_ALLOWED)
        
