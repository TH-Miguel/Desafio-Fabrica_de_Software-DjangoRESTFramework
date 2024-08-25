from rest_framework import viewsets
from apirickmorty.API import serializers
from apirickmorty import models 

class CharactersViewSet(viewsets.ModelViewSet):
    serializers_class = serializers.CharactersSerializer
    queryset = models.Characters.objects.all()

    