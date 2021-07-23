from django.db import models

class Titulo(models.Model):
   idtitulo =  models.AutoField(primary_key=True, verbose_name="idTitlo")
   titulo = models.CharField(max_length=60, null=False, blank = False, verbose_name="Titulo")
   sinopse = models.TextField(max_length=300, null=False, blank = False, verbose_name="Sinopse")
   ano = models.IntegerField(null=False, blank = False, verbose_name="Ano")

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

class Episodio(models.Model):
    id_ep = models.AutoField(primary_key=True)
    numero = models.IntegerField(null=False, blank=False, verbose_name="Numero Episódio")
    titulo_ep = models.CharField(max_length=60, null=False, blank = False, verbose_name="Titulo Episódio")
    sinopse_ep = models.TextField(max_length=1000, null=False, blank = False, verbose_name="Sinopse do Episódio")
    temporada = models.IntegerField(null=False, blank=False, verbose_name="Temporada")
    fk_serie = models.ForeignKey('Serie', db_column='titulo_ptr_id', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Episodio'
        verbose_name_plural = 'Episodios'
        db_table = 'episodio'

    def __str__(self):
        return  self.fk_serie
