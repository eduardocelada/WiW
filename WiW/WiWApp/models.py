from django.db import models

# Create your models here.

class Perfil(models.Model):
	IdPerfil=models.AutoField(primary_key=True)
	nombre_completo = models.CharField(max_length=70)
	fdn=models.DateTimeField()
	email=models.EmailField()
	ciudad=models.CharField()
	estado=models.CharField()
	pais=models.CharField()
	twitter=models.CharField(max_length=15)
	facebookid=models.IntegerField()
	passw=models.CharField()

class Posts(models.Model):
	idPost=models.AutoField(primary_key=True)
	FechaPost=models.datetime.auto_now_add=True
	IdPerfil=models.ForeignKey('Perfil')
	urlImg=models.URLField()

class Comentarios(models.Model):
	idComentario=models.AutoField(primary_key=True)
	Comentador=models.ForeignKey('Perfil')
	Comentario=models.CharField()

class Likes(models.Model):
	idLike=models.AutoField()
	idPost=models.ForeignKey('Posts')
	IdPerfil=models.ForeignKey('Perfil')

class Estilo(models.Model):
	idEstilo=models.AutoField(primary_key=True)
	Estilo=models.CharField()

class Colores(models.Model):
	idColores=models.AutoField(primary_key=True)
	Colores=models.CharField()

class EstiloPerfil(models.Model):
	idRelacion=models.AutoField()
	IdPerfil=ForeignKey('Perfil')
	idEstilo=ForeignKey('Estilo')
	idColores=ForeignKey('Colores')



