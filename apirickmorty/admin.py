from django.contrib import admin
from .models import Characters

@admin.register(Characters)
class NameAdmin(admin.ModelAdmin):
    list_display = ('id','name','status','species','type','gender','origin','location','episode','url','create') ##### List display representa os parametros que vao aparecer no ADMIN para criar novas atribuições para o banco de dados
