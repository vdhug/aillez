from django.shortcuts import render
from .models import Sobre

# Create your views here.
def sobre(request):
    sobre = Sobre.objects.all().first()
    context = {
        "sobre": sobre
    }
    return render(request, "sobre/sobre.html", context)