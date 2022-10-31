# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.conf import settings
from comparador.models import TotalizacaoCandidato
from django.conf import settings

# Importa arquivo de votação nominal
class Command(BaseCommand):
    def handle(self, *args, **options):
        path = '{0}/{1}'.format(settings.BASE_DIR,'dados_tse_deputado_federal_ma.csv')
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                print (row)
                _, created = TotalizacaoCandidato.objects.get_or_create(
                    sg_uf = row[0],
                    cd_cargo = row[1],
                    ds_cargo = row[2],
                    nr_candidato = row[3],
                    nm_candidato = row[4],
                    nm_urna_candidato = row[5],
                    sg_partido = row[6],
                    ds_composicao_coligacao = row[7],
                    nr_turno = row[8],
                    ds_sit_totalizacao = row[9],
                    dt_ult_totalizacao = row[10],
                    sg_ue = row[11],
                    sq_candidato = row[12],
                    nm_tipo_destinacao_votos = row[13],
                    sq_eleicao_divulga = row[14],
                    qt_votos_nom_validos = row[15],
                    qt_votos_concorrentes = row[16],
                    )