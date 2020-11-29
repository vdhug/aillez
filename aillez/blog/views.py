from .models import Estudo
from django.shortcuts import render

# Create your views here.
def index(request):
    estudos = Estudo.objects.all()
    context = {
        "estudos": estudos
    }
    return render(request, "blog/estudos.html", context)

def estudo(request, slug):
    estudo = Estudo.objects.filter(slug=slug).first()
    context = {
        "estudo": estudo
    }
    return render(request, "blog/estudo.html", context)