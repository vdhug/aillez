from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

# Create your models here.
class Estudo(models.Model):
    slug = models.SlugField(blank=True, null=True)
    nome = models.CharField(blank=True, null=True, max_length=180, verbose_name="Nome do estudo de caso.")
    trabalho_feito = models.CharField(blank=True, null=True, max_length=260, verbose_name="Trabalho realizado")
    cliente = models.CharField(blank=True, null=True, max_length=260, verbose_name="Nome do cliente")
    titulo_cliente = models.CharField(blank=True, null=True, max_length=260, verbose_name="Titulo do cliente")
    depoimento = models.TextField(blank=True, null=True, verbose_name="Depoimento do cliente")
    breve_descricao = models.TextField(blank=True, null=True, verbose_name="Breve descrição do estudo de caso.")
    descricao_detalhada = RichTextField(blank=True, null=True, verbose_name="Descrição detalhada do estudo de caso.")
    estudo_imagem = models.ImageField(
        upload_to='uploads/estudos/%Y/%m/', verbose_name="Imagem do estudo (600X1900)", default="")

    class Meta:
        verbose_name_plural = "Estudos de caso."
    
    def __str__(self) -> str:
        return f"{self.nome}"
    
    def save(self, *args, **kwargs):
        # Newly created object, so set slug
        self.slug = slugify(self.nome)

        super(Estudo, self).save(*args, **kwargs)