from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/estudos.html")

def estudo(request, slug):
    return render(request, "blog/estudo.html")