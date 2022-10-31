from django.db import models

# Modelo que guarda o Total de Votos em Legenda importados dos Dados em CSV do TSE
class TotalizacaoLegenda(models.Model):
    ds_composicao_coligacao = models.CharField(blank=True, max_length=255)
    qt_votos_leg_validos = models.IntegerField(default=0)
    qt_votos_nom_validos = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Totalização votos em Legenda Dados TSE)'
        verbose_name_plural = 'Totalizações votos em Legenda (Dados TSE)'

    def __str__(self):
        return self.ds_composicao_coligacao

# Modelo que guarda o Total de Votos Nominais importados dos Dados em CSV do TSE
class TotalizacaoCandidato(models.Model):
    sg_uf = models.CharField(blank=True, max_length=255)
    cd_cargo = models.CharField(blank=True, max_length=255)
    ds_cargo = models.CharField(blank=True, max_length=255)
    nr_candidato = models.CharField(blank=True, max_length=255)
    nm_candidato = models.CharField(blank=True, max_length=255)
    nm_urna_candidato = models.CharField(blank=True, max_length=255)
    sg_partido = models.CharField(blank=True, max_length=255)
    ds_composicao_coligacao = models.CharField(blank=True, max_length=255)
    nr_turno = models.CharField(blank=True, max_length=255)
    ds_sit_totalizacao = models.CharField(blank=True, max_length=255)
    dt_ult_totalizacao = models.CharField(blank=True, max_length=255)
    sg_ue = models.CharField(blank=True, max_length=255)
    sq_candidato = models.CharField(blank=True, max_length=255)
    nm_tipo_destinacao_votos = models.CharField(blank=True, max_length=255)
    sq_eleicao_divulga = models.CharField(blank=True, max_length=255)
    qt_votos_nom_validos = models.IntegerField(default=0)
    qt_votos_concorrentes = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Totalização por Candidato (Dados TSE)'
        verbose_name_plural = 'Totalizações por Candidato (Dados TSE)'

    def __str__(self):
        return self.nome_urna_candidato

# Modelo que totaliza os votos dos partidos (Nominais e Legendas) e guarda os dados de quociente calculados pelo sistema
class TotalizacaoPartido(models.Model):
    ds_composicao_coligacao = models.CharField(blank=True, max_length=255)
    qt_votos_validos = models.IntegerField(default=0)
    qt_votos_concorrentes = models.IntegerField(default=0)
    qe = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    qp = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    vagas_obtidas_algoritmo_tse = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    vagas_obtidas_algoritmo_corrigido = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    class Meta:
        verbose_name = 'Totalização por Partido/Federação'
        verbose_name_plural = 'Totalizações por Partido/Federação'

    def __str__(self):
        return self.ds_composicao_coligacao

# Modelo que guarda os resultados da simulação do algoritmo do TSE
class ResultadoSimulacaoTSE(models.Model):
    TIPO_ELEITO = (
        ('sobras', 'Eleito Por Média (Sobras)'),
        ('eleito_por_quociente', 'Eleito por Quociente'),
    )

    cd_cargo = models.CharField(blank=True, max_length=255)
    ds_cargo = models.CharField(blank=True, max_length=255)
    nr_candidato = models.CharField(blank=True, max_length=255)
    nm_candidato = models.CharField(blank=True, max_length=255)
    nm_urna_candidato = models.CharField(blank=True, max_length=255)
    sg_partido = models.CharField(blank=True, max_length=255)
    ds_composicao_coligacao = models.CharField(blank=True, max_length=255)
    ds_sit_totalizacao = models.CharField(blank=True, max_length=255)
    qt_votos_nom_validos = models.IntegerField()
    tipo_eleito = models.CharField(choices=TIPO_ELEITO, max_length=50)

    class Meta:
        verbose_name = 'Resultado Simulacao TSE'
        verbose_name_plural = 'Resultados Simulacao TSE'

    def __str__(self):
        return self.nm_urna_candidato

# Modelo que guarda os resultados da simulação Corrigida - Consideração Artigo 109 - inciso I
class ResultadoSimulacaoCorrigida(models.Model):
    TIPO_ELEITO = (
        ('sobras', 'Eleito Por Média (Sobras)'),
        ('eleito_por_quociente', 'Eleito por Quociente'),
    )

    cd_cargo = models.CharField(blank=True, max_length=255)
    ds_cargo = models.CharField(blank=True, max_length=255)
    nr_candidato = models.CharField(blank=True, max_length=255)
    nm_candidato = models.CharField(blank=True, max_length=255)
    nm_urna_candidato = models.CharField(blank=True, max_length=255)
    sg_partido = models.CharField(blank=True, max_length=255)
    ds_composicao_coligacao = models.CharField(blank=True, max_length=255)
    sq_eleicao_divulga = models.CharField(blank=True, max_length=255)
    ds_sit_totalizacao = models.CharField(blank=True, max_length=255)
    qt_votos_nom_validos = models.IntegerField()
    tipo_eleito = models.CharField(choices=TIPO_ELEITO, max_length=50)

    class Meta:
        verbose_name = 'Resultados Simulacao Correta (Consideração Artigo 109 - inciso I)'
        verbose_name_plural = 'Resultado Simulacao Correta (Consideração Artigo 109 - inciso I)'

    def __str__(self):
        return self.nm_urna_candidato