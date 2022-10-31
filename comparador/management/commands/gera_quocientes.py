# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import csv
from comparador.models import TotalizacaoPartido
from django.db.models import Sum
from django.conf import settings
import pandas as pd
import csv

# Gera quociente eleitoral e partidario
class Command(BaseCommand):
    def handle(self, *args, **options):
        votosvalidos = TotalizacaoPartido.objects.all().aggregate(Sum('qt_votos_validos'))['qt_votos_validos__sum']
        qe = round(votosvalidos / settings.VAGAS_DEPUTADO_2022) #round arredonda para mais se acima de 0,5  
        partidos = TotalizacaoPartido.objects.all()
        partidos.update(qe=round(qe))
        for partido in partidos:
            qp =  int(partido.qt_votos_validos / qe) #conversão para inteiro para desprezar  a fração
            partido.qp = qp
            partido.save()
            print (qp)
        print (qe)