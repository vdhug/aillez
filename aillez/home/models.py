from django.db import models


class PaginaHome(models.Model):
    title = models.CharField(
        max_length=80,  verbose_name="Título", default="Informações que estão presentes na página home.")
    slogan = models.CharField(max_length=160,  verbose_name="Slogan da empresa")

    sobre_titulo = models.CharField(max_length=160,  verbose_name="Sobre titulo")
    sobre_descricao = models.TextField(verbose_name="Sobre descrição")
    sobre_time = models.ImageField(
        upload_to='uploads/home/%Y/%m/', verbose_name="Foto do time divulgação (100x100)", default="")

    class Meta:
        verbose_name_plural = "Pagina Home"


class PaginaSobre(models.Model):
    title = models.CharField(
        max_length=80,  verbose_name="Título", default="Informações que estão presentes na página sobre.")
    titulo = models.CharField(max_length=160,  verbose_name="Titulo")
    sobre_descricao = models.TextField(verbose_name="Descrição")


class Conquista(models.Model):
    descricao = models.CharField(max_length=160,  verbose_name="Descriçao da conquista (e.g. Mais de 20 projetos executados)")


class PaginaServico(models.Model):
    title = models.CharField(
        max_length=80,  verbose_name="Título", default="Informações que estão presentes na página de serviços.")
    titulo = models.CharField(max_length=160,  verbose_name="Titulo")
    descricao = models.TextField(verbose_name="Descrição")


class PaginaContato(models.Model):
    title = models.CharField(
        max_length=80,  verbose_name="Título", default="Informações que estão presentes na página de contato.")
    cidade = models.CharField(max_length=160,  verbose_name="Cidade que o escritório está localizado")
    rua = models.CharField(max_length=160,  verbose_name="Rua que o escritório está localizado")
    bairro = models.CharField(max_length=160,  verbose_name="Bairro que o escritório está localizado")
    cep = models.CharField(max_length=160,  verbose_name="CEP que o escritório está localizado")
    numero = models.CharField(max_length=160,  verbose_name="Numero que o escritório está localizado")
    telefone = models.CharField(max_length=160,  verbose_name="Telefone para contato do escritório")
    email = models.EmailField(verbose_name="Email para contato.")
    imagem_escritório = models.ImageField(
        upload_to='uploads/servicos/%Y/%m/', verbose_name="Foto de divulgação do serviço (650x400)", default="")


class Servico(models.Model):
    titulo = models.CharField(max_length=160,  verbose_name="Título do serviço")
    descricao = models.TextField(verbose_name="Descrição do serviço")
    imagem = models.ImageField(
        upload_to='uploads/servicos/%Y/%m/', verbose_name="Foto de divulgação do serviço (400x350)", default="")


class EstudoDeCaso(models.Model):
    titulo = models.CharField(max_length=160,  verbose_name="Título do serviço")
    trabalho_realizado = models.TextField(verbose_name="Trabalho realizado")
    breve_descricao = models.TextField(verbose_name="Breve descrição do serviço realizado")
    imagem = models.ImageField(
        upload_to='uploads/estudos/%Y/%m/', verbose_name="Foto de divulgação do serviço (650x500)", default="")


class Paragrafo(models.Model):
    texto = models.TextField(verbose_name="Texto do parágrafo")
