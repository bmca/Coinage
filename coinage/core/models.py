from django.db import models

# Create your models here.

class Game(models.Model):
	titulo = models.CharField(max_length=100)
	descricao = models.TextField()
	imagem = models.ImageField(upload_to='games')
	nota = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
	precoSteam = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	precoOrigin = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	precoNuuvem = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	precoHumbleStore = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	precoGOG = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	precoGMG = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)

	def __unicode__(self):
		return self.titulo

class Usuario(models.Model):
	nome = models.CharField(max_length=100)
	email = models.EmailField(verbose_name='e-mail')
	colecao = models.ManyToManyField(Game, blank=True, related_name='colecao')
	wishlist = models.ManyToManyField(Game, blank=True, related_name='wishlist')

	def __unicode__(self):
		return self.nome

class Comentario(models.Model):
	usuario = models.ForeignKey(Usuario)
	critica = models.TextField()
	jogo = models.ForeignKey(Game)

	def __unicode__(self):
		return u'%s %s' % (self.usuario.nome, self.jogo.titulo)