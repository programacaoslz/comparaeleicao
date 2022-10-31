# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.conf import settings
from comparador.models import TotalizacaoPartido, ResultadoSimulacaoTSE, TotalizacaoCandidato
from django.db.models import Sum
from django.conf import settings
from decimal import Decimal
from django.db.models import F

# Classificação dos Eleitores pela Lógica Equivalente ao do TSE
class Command(BaseCommand):
    def handle(self, *args, **options):
        
        partidos = TotalizacaoPartido.objects.all()
        ResultadoSimulacaoTSE.objects.all().delete() #limpa para começar de novo
        #reinicia as vagas obtidas 
        for partido in partidos:
            partido.vagas_obtidas_algoritmo_tse = partido.qp
            partido.save()

        qe = None
        if not qe:
            qe = partidos.first().qe

        # calculo de 80% do quociente para eliminar os partidos não aptos
        qe80 = qe * Decimal(0.8)
        # calculo de 20% do quociente para eliminar os candidatos não aptos
        qe20 = qe * Decimal(0.2)
        # calculo de 10% do quociente para eliminar os candidatos não aptos
        qe10 = qe * Decimal(0.1)

        # classifica os candidatos por quociente partidario
        for partido in partidos:
            # filtrando apenas candidatos com mais de 10% do 
            candidatospartido = TotalizacaoCandidato.objects.filter(qt_votos_nom_validos__gte=qe10, ds_composicao_coligacao=partido.ds_composicao_coligacao).order_by('-qt_votos_nom_validos')[:partido.qp] #traz os candidatos da coligação ordenados pela maior quantidade de votos e apenas a quantidade de vagas

            for c in candidatospartido:
                ResultadoSimulacaoTSE.objects.get_or_create(
                        cd_cargo = c.cd_cargo,
                        ds_cargo = c.ds_cargo,
                        nr_candidato = c.nr_candidato,
                        nm_candidato = c.nm_candidato,
                        nm_urna_candidato = c.nm_urna_candidato,
                        sg_partido = c.sg_partido,
                        ds_composicao_coligacao = c.ds_composicao_coligacao,
                        ds_sit_totalizacao = c.ds_sit_totalizacao,
                        qt_votos_nom_validos = c.qt_votos_nom_validos,
                        tipo_eleito = 'eleito_por_quociente',
                )

            #Atualiza numero de vagas preenchidas
            partido.vagas_obtidas_algoritmo_tse = partido.qp
            partido.save()
            # salva em variavel o qe para uso posterior

        #numero de vagas que sobraram
        vagas_remanescentes = int(settings.VAGAS_DEPUTADO_2022 - TotalizacaoPartido.objects.all().aggregate(Sum('vagas_obtidas_algoritmo_tse'))['vagas_obtidas_algoritmo_tse__sum'])
        #print (vagas_remanescentes)
        
        partidos_ignorar = []      

        #Calculo de sobras 
        for i in range(1,vagas_remanescentes + 1):
            #print(i)
            #traz o partido com melhor quociente excluindo-se os que não tem candidatos que atingiram os 20%
            partido = TotalizacaoPartido.objects.filter(qt_votos_validos__gte=qe80).annotate(votacao_vagas=F('qt_votos_validos')/(F('vagas_obtidas_algoritmo_tse') + 1)).exclude(ds_composicao_coligacao__in=partidos_ignorar).order_by('-votacao_vagas')[0]

            #obtem os candidatos eleitos para excluir da distribuição
            candidatos_eleitos = ResultadoSimulacaoTSE.objects.all().values_list('nr_candidato', flat=True)

            # distribui cada vaga para o partido selecionado acima
            if partido:
                # pega os candidatos que atingiram 20% e que ainda não foram eleitos pelo algoritmo
                candidatospartido = TotalizacaoCandidato.objects.filter(qt_votos_nom_validos__gte=qe20, ds_composicao_coligacao=partido.ds_composicao_coligacao).exclude(nr_candidato__in=candidatos_eleitos).order_by('-qt_votos_nom_validos')[0] #traz o candidato com mais votos no partido e que tenha mais de 20%
                if candidatospartido:
                    ResultadoSimulacaoTSE.objects.get_or_create(
                    cd_cargo = candidatospartido.cd_cargo,
                    ds_cargo = candidatospartido.ds_cargo,
                    nr_candidato = candidatospartido.nr_candidato,
                    nm_candidato = candidatospartido.nm_candidato,
                    nm_urna_candidato = candidatospartido.nm_urna_candidato,
                    sg_partido = candidatospartido.sg_partido,
                    ds_composicao_coligacao = candidatospartido.ds_composicao_coligacao,
                    ds_sit_totalizacao = candidatospartido.ds_sit_totalizacao,
                    qt_votos_nom_validos = candidatospartido.qt_votos_nom_validos,
                    tipo_eleito = 'sobras',
                    ) 
                    # diminui uma vaga
                    partido.vagas_obtidas_algoritmo_tse += 1 
                    partido.save()
                    #print (vagas_remanescentes)
                else:
                    partidos_ignorar.append(partido.ds_composicao_coligacao)
                    #print (partidos_ignorar)
