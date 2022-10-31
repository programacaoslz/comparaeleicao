# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from comparador.models import TotalizacaoLegenda, TotalizacaoCandidato, TotalizacaoPartido
from django.db.models import Sum

class Command(BaseCommand):
    def handle(self, *args, **options):
        total = TotalizacaoCandidato.objects.all()
        TotalizacaoPartido.objects.all().delete()
        # Totaliza votos nominais
        for tc in total:            
            tp = TotalizacaoPartido.objects.get_or_create(ds_composicao_coligacao=tc.ds_composicao_coligacao)[0]
            if tp:
                tp.qt_votos_validos = tp.qt_votos_validos + tc.qt_votos_nom_validos
                tp.save()

        # Totaliza votos em legendas
        legendas = TotalizacaoLegenda.objects.all()
        for leg in legendas:
            tp = TotalizacaoPartido.objects.get_or_create(ds_composicao_coligacao=leg.ds_composicao_coligacao)[0]
            if tp:
                tp.qt_votos_validos = tp.qt_votos_validos + leg.qt_votos_leg_validos
                tp.save()

        # Atualiza campo de total geral que vai ser usado depois
        totalpartidos = TotalizacaoPartido.objects.all().aggregate(Sum('qt_votos_validos'))['qt_votos_validos__sum']
        partidos = TotalizacaoPartido.objects.all()
        partidos.update(qt_votos_concorrentes=totalpartidos)
