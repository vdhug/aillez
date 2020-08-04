from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "home/index.html")


def sobre(request):
    return render(request, "sobre/sobre.html")


def servicos(request):
    return render(request, "servicos/servicos.html")


def contato(request):
    return render(request, "contato/contato.html")


def estudos(request):
    return render(request, "estudos/estudos.html")