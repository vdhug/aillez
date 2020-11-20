from django.db import models
from ckeditor.fields import RichTextField


class Servico(models.Model):
    nome = models.CharField(blank=True, null=True, max_length=180, verbose_name="Nome do serviço.")
    breve_descricao = models.TextField(blank=True, null=True, verbose_name="Breve descrição do serviço.")
    descricao_detalhada = RichTextField(blank=True, null=True, verbose_name="Descrição detalhada do serviço.")
    servico_imagem = models.ImageField(
        upload_to='uploads/servicos/%Y/%m/', verbose_name="Imagem do serviço (630X550)", default="")

    class Meta:
        verbose_name_plural = "Serviços oferecidos"
    
    def __str__(self) -> str:
        return f"{self.nome}"