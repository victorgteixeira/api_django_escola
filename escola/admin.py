from django.contrib import admin
from escola.models import Estudante, Curso, Matricula

class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
    search_fields = ('nome', 'cpf',)

admin.site.register(Estudante, EstudanteAdmin)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Curso)


class Matriculas(admin.ModelAdmin):
    list_display = ('id','estudante','curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula,Matriculas)
