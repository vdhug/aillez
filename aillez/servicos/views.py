from .models import Servico
from django.shortcuts import render

# Create your views here.
def servicos(request):
    servicos = Servico.objects.all()
    context = {
        "servicos": servicos
    }
    return render(request, "servicos/servicos.html", context)


def servico(request, slug):
    servico = Servico.objects.filter(slug=slug).first()
    context = {
        "servico": servico
    }
    return render(request, "servicos/servico.html", context)