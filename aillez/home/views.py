from .models import PaginaHome
from django.shortcuts import render


# Create your views here.
def index(request):
    home_info = PaginaHome.objects.all().first()
    return render(request, "home/index.html", {'home_info': home_info})

def servicos(request):
    return render(request, "servicos/servicos.html")


def servico(request, slug):
    return render(request, "servicos/servico.html")


def contato(request):
    return render(request, "contato/contato.html")


def estudos(request):
    return render(request, "estudos/estudos.html")