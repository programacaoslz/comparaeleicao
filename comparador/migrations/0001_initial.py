# Generated by Django 3.2.8 on 2022-10-31 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResultadoSimulacaoCorrigida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_cargo', models.CharField(blank=True, max_length=255)),
                ('ds_cargo', models.CharField(blank=True, max_length=255)),
                ('nr_candidato', models.CharField(blank=True, max_length=255)),
                ('nm_candidato', models.CharField(blank=True, max_length=255)),
                ('nm_urna_candidato', models.CharField(blank=True, max_length=255)),
                ('sg_partido', models.CharField(blank=True, max_length=255)),
                ('ds_composicao_coligacao', models.CharField(blank=True, max_length=255)),
                ('sq_eleicao_divulga', models.CharField(blank=True, max_length=255)),
                ('ds_sit_totalizacao', models.CharField(blank=True, max_length=255)),
                ('qt_votos_nom_validos', models.IntegerField()),
                ('tipo_eleito', models.CharField(choices=[('sobras', 'Eleito Por Média (Sobras)'), ('eleito_por_quociente', 'Eleito por Quociente')], max_length=50)),
            ],
            options={
                'verbose_name': 'Resultados Simulacao Correta (Consideração Artigo 109 - inciso I)',
                'verbose_name_plural': 'Resultado Simulacao Correta (Consideração Artigo 109 - inciso I)',
            },
        ),
        migrations.CreateModel(
            name='ResultadoSimulacaoTSE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_cargo', models.CharField(blank=True, max_length=255)),
                ('ds_cargo', models.CharField(blank=True, max_length=255)),
                ('nr_candidato', models.CharField(blank=True, max_length=255)),
                ('nm_candidato', models.CharField(blank=True, max_length=255)),
                ('nm_urna_candidato', models.CharField(blank=True, max_length=255)),
                ('sg_partido', models.CharField(blank=True, max_length=255)),
                ('ds_composicao_coligacao', models.CharField(blank=True, max_length=255)),
                ('ds_sit_totalizacao', models.CharField(blank=True, max_length=255)),
                ('qt_votos_nom_validos', models.IntegerField()),
                ('tipo_eleito', models.CharField(choices=[('sobras', 'Eleito Por Média (Sobras)'), ('eleito_por_quociente', 'Eleito por Quociente')], max_length=50)),
            ],
            options={
                'verbose_name': 'Resultado Simulacao TSE',
                'verbose_name_plural': 'Resultados Simulacao TSE',
            },
        ),
        migrations.CreateModel(
            name='TotalizacaoCandidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sg_uf', models.CharField(blank=True, max_length=255)),
                ('cd_cargo', models.CharField(blank=True, max_length=255)),
                ('ds_cargo', models.CharField(blank=True, max_length=255)),
                ('nr_candidato', models.CharField(blank=True, max_length=255)),
                ('nm_candidato', models.CharField(blank=True, max_length=255)),
                ('nm_urna_candidato', models.CharField(blank=True, max_length=255)),
                ('sg_partido', models.CharField(blank=True, max_length=255)),
                ('ds_composicao_coligacao', models.CharField(blank=True, max_length=255)),
                ('nr_turno', models.CharField(blank=True, max_length=255)),
                ('ds_sit_totalizacao', models.CharField(blank=True, max_length=255)),
                ('dt_ult_totalizacao', models.CharField(blank=True, max_length=255)),
                ('sg_ue', models.CharField(blank=True, max_length=255)),
                ('sq_candidato', models.CharField(blank=True, max_length=255)),
                ('nm_tipo_destinacao_votos', models.CharField(blank=True, max_length=255)),
                ('sq_eleicao_divulga', models.CharField(blank=True, max_length=255)),
                ('qt_votos_nom_validos', models.IntegerField(default=0)),
                ('qt_votos_concorrentes', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Totalização por Candidato (Dados TSE)',
                'verbose_name_plural': 'Totalizações por Candidato (Dados TSE)',
            },
        ),
        migrations.CreateModel(
            name='TotalizacaoLegenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds_composicao_coligacao', models.CharField(blank=True, max_length=255)),
                ('qt_votos_leg_validos', models.IntegerField(default=0)),
                ('qt_votos_nom_validos', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Totalização votos em Legenda Dados TSE)',
                'verbose_name_plural': 'Totalizações votos em Legenda (Dados TSE)',
            },
        ),
        migrations.CreateModel(
            name='TotalizacaoPartido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds_composicao_coligacao', models.CharField(blank=True, max_length=255)),
                ('qt_votos_validos', models.IntegerField(default=0)),
                ('qt_votos_concorrentes', models.IntegerField(default=0)),
                ('qe', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('qp', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('vagas_obtidas_algoritmo_tse', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('vagas_obtidas_algoritmo_corrigido', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'verbose_name': 'Totalização por Partido/Federação',
                'verbose_name_plural': 'Totalizações por Partido/Federação',
            },
        ),
    ]