from django.db import models
from home.models import Paragrafo

# Create your models here.
class SobreNos(models.Model):
    paragrafos = models.ManyToManyField(Paragrafo)

class Compromisso(models.Model):
    paragrafos = models.ManyToManyField(Paragrafo)