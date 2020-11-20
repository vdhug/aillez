from .models import PaginaHome
from django.shortcuts import render


# Create your views here.
def index(request):
    home_info = PaginaHome.objects.all().first()
    return render(request, "home/index.html", {'home_info': home_info})


def contato(request):
    return render(request, "contato/contato.html")
