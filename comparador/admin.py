from django.contrib import admin
from .models import TotalizacaoCandidato, TotalizacaoPartido, ResultadoSimulacaoTSE, ResultadoSimulacaoCorrigida, TotalizacaoLegenda

class TotalizacaoLegendaAdmin(admin.ModelAdmin):
    list_display = ('ds_composicao_coligacao', 'qt_votos_leg_validos', 'qt_votos_nom_validos')
    ordering = ('ds_composicao_coligacao',)

class TotalizacaoCandidatoAdmin(admin.ModelAdmin):
    list_display = ('nr_candidato', 'nm_urna_candidato', 'sg_partido', 'ds_composicao_coligacao', 'qt_votos_nom_validos', 'qt_votos_concorrentes')
    search_fields = ('nm_candidato',)
    list_filter = ('sg_partido', 'ds_composicao_coligacao')
    ordering = ('nm_urna_candidato',)

class TotalizacaoPartidoAdmin(admin.ModelAdmin):
    list_display = ('ds_composicao_coligacao', 'qt_votos_validos', 'qt_votos_concorrentes', 'qe', 'qp', 'vagas_obtidas_algoritmo_tse', 'vagas_obtidas_algoritmo_corrigido')
    list_filter = ('ds_composicao_coligacao',)
    ordering = ('ds_composicao_coligacao',)

class ResultadoSimulacaoTSEAdmin(admin.ModelAdmin):
    list_display = ('nr_candidato', 'nm_urna_candidato', 'nm_candidato', 'sg_partido', 'ds_composicao_coligacao', 'qt_votos_nom_validos', 'tipo_eleito')
    search_fields = ('nm_candidato',)
    list_filter = ('sg_partido',)
    ordering = ('-qt_votos_nom_validos',)

class ResultadoSimulacaoCorrigidaAdmin(admin.ModelAdmin):
    list_display = ('nr_candidato', 'nm_urna_candidato', 'nm_candidato', 'sg_partido', 'ds_composicao_coligacao', 'qt_votos_nom_validos', 'tipo_eleito')
    search_fields = ('nm_candidato',)
    list_filter = ('sg_partido',)
    ordering = ('-qt_votos_nom_validos',)

admin.site.register(TotalizacaoLegenda, TotalizacaoLegendaAdmin)
admin.site.register(TotalizacaoCandidato, TotalizacaoCandidatoAdmin)
admin.site.register(TotalizacaoPartido, TotalizacaoPartidoAdmin)
admin.site.register(ResultadoSimulacaoTSE, ResultadoSimulacaoTSEAdmin)
admin.site.register(ResultadoSimulacaoCorrigida, ResultadoSimulacaoCorrigidaAdmin)
