from django.db import models

class Titulo(models.Model):
   idtitulo =  models.AutoField(primary_key=True, verbose_name="idTitlo")
   titulo = models.CharField(max_length=60, null=False, blank = False, verbose_name="Titulo")
   sinopse = models.TextField(max_length=300, null=False, blank = False, verbose_name="Sinopse")
   ano = models.IntegerField(null=False, blank = False, verbose_name="Sinopse")

   class Meta:
        verbose_name = 'Titulo'
        verbose_name_plural = 'Titulos'
        db_table = 'titulo'

class Serie(Titulo):
    anofim = models.IntegerField( null=True, verbose_name='AnoFim')
    
    class Meta:
        verbose_name = 'Serie'
        verbose_name_plural = 'Series'
        db_table = 'serie'

class Filme(Titulo):
    datalancamento = models.DateField(null=False, verbose_name="Data de Lançamento")

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        db_table = 'filme'

class Episodio(Serie):
    numero = models.AutoField(primary_key=True, verbose_name="Numero Episódio")
    titulo_ep = models.CharField(max_length=60, null=False, blank = False, verbose_name="Titulo Episódio")
    sinopse_ep = models.TextField(max_length=300, null=False, blank = False, verbose_name="Sinopse do Episódio")
    temporada = models.IntegerField(null=False, blank=False, verbose_name="Temporada")

    class Meta:
        verbose_name = 'Episodio'
        verbose_name_plural = 'Episodios'
        db_table = 'episodio'

