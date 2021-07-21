# Generated by Django 3.2.3 on 2021-07-21 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('idtitulo', models.AutoField(primary_key=True, serialize=False, verbose_name='idTitlo')),
                ('titulo', models.CharField(max_length=60, verbose_name='Titulo')),
                ('sinopse', models.TextField(max_length=300, verbose_name='Sinopse')),
                ('ano', models.IntegerField(verbose_name='Ano')),
                ('tipo', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Titulo',
                'verbose_name_plural': 'Titulos',
                'db_table': 'titulo',
            },
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('titulo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Primeflix.titulo')),
                ('datalancamento', models.DateField(verbose_name='Data de Lançamento')),
            ],
            options={
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
                'db_table': 'filme',
            },
            bases=('Primeflix.titulo',),
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('titulo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Primeflix.titulo')),
                ('anofim', models.IntegerField(null=True, verbose_name='AnoFim')),
            ],
            options={
                'verbose_name': 'Serie',
                'verbose_name_plural': 'Series',
                'db_table': 'serie',
            },
            bases=('Primeflix.titulo',),
        ),
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('serie_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='Primeflix.serie')),
                ('numero', models.AutoField(primary_key=True, serialize=False, verbose_name='Numero Episódio')),
                ('titulo_ep', models.CharField(max_length=60, verbose_name='Titulo Episódio')),
                ('sinopse_ep', models.TextField(max_length=300, verbose_name='Sinopse do Episódio')),
                ('temporada', models.IntegerField(verbose_name='Temporada')),
            ],
            options={
                'verbose_name': 'Episodio',
                'verbose_name_plural': 'Episodios',
                'db_table': 'episodio',
            },
            bases=('Primeflix.serie',),
        ),
    ]
