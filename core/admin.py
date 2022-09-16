from django.contrib import admin

from .models import Cargo, Feature, Funcionario, Plano, Servico, Testemunho


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature', 'icone', 'ativo', 'modificado', 'lado')


@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('plano', 'icone', 'ativo', 'modificado', 'destaque')


@admin.register(Testemunho)
class TestemunhoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado', 'nota')
