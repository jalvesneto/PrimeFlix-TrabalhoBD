# Generated by Django 3.2.3 on 2021-07-21 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Primeflix', '0003_titulo_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='titulo',
            name='tipo',
        ),
    ]