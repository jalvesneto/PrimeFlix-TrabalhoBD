# Generated by Django 3.2.3 on 2021-07-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Primeflix', '0002_auto_20210723_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False, verbose_name='idUser')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('senha', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuario',
            },
        ),
    ]
