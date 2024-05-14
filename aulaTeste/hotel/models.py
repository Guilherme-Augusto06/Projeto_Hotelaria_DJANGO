from django.db import models

# Create your models here.
TIPOS_QUARTO = (
    ("SOLTEIRO", "Solteiro"),
    ("CASAL", "Casal"),
    ("CONFORT","Confort"),
    ("LUXO","Luxo")
     
)

class Hotel(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.titulo

class Quarto(models.Model):
    tipo = models.CharField(max_length=50, choices=TIPOS_QUARTO)
    disponibilidade = models.IntegerField()
    valor = models.FloatField(max_length=4)
    descricao = models.TextField(max_length=255)
    foto_quarto = models.ImageField(upload_to='foto_quartos/')

    def __str__(self):
        return self.tipo