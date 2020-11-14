from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class SobreNos(models.Model):
    title = models.CharField(
        max_length=80,  verbose_name="Título", default="Escreva sobre a empresa")
    texto = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Sobre a empresa"

class Compromisso(models.Model):
    title = models.CharField(
        max_length=80,  verbose_name="Título", default="Escreva sobre os compromissos da empresa")
    texto = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Compromissos da empresa"