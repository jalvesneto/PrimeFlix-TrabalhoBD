# Generated by Django 3.2.3 on 2021-07-21 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Primeflix', '0002_remove_titulo_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='titulo',
            name='tipo',
            field=models.CharField(default='titulo', max_length=60),
        ),
    ]
