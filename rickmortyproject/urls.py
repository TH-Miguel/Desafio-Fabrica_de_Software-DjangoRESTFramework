"""
URL configuration for rickmortyproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers #### Utilizei essa importação que ja possui pelo próprio django rest que tem como função definir as rotas espécificas que eu quero que minha aplicação esteja
from apirickmorty.views import RickAndMortyViewSet   ##### importei minhas views que foi criada na pasta de meu aplicativo apirickmorty views.py 

route = routers.DefaultRouter()   ####### utizilei a router default 

route.register(r'rickandmorty', RickAndMortyViewSet, basename='rickandmorty')   ###### registrei uma nova rota que minha aplicação ira aparecer



urlpatterns = [
    path('admin/', admin.site.urls),
   path('', include(route.urls)) 
]   

