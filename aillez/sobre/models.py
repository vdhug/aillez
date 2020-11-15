from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Sobre(models.Model):
    title = models.CharField(
        max_length=80,  verbose_name="Título", default="Escreva sobre a empresa")
    sobre_nos = RichTextField(blank=True, null=True, verbose_name="Escreva sobre a empresa")
    compromissos = RichTextField(blank=True, null=True, verbose_name="Escreva sobre os compromissos da empresa")

    class Meta:
        verbose_name_plural = "Sobre a empresa"
