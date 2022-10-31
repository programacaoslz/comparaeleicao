# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.conf import settings
from comparador.models import TotalizacaoLegenda
from django.conf import settings

# Importa arquivo de votação em legenda
class Command(BaseCommand):
    def handle(self, *args, **options):
        path = '{0}/{1}'.format(settings.BASE_DIR,'dados_tse_deputado_federal_ma_legenda.csv')
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                print (row)
                _, created = TotalizacaoLegenda.objects.get_or_create(
                    ds_composicao_coligacao = row[0],
                    qt_votos_leg_validos = row[1],
                    qt_votos_nom_validos = row[2],
                    )