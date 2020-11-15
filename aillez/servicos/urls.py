from django.urls import path

from . import views

urlpatterns = [
    path("", views.servicos, name="servicos"),
    path("<slug:slug>/", views.servico, name="servico"),
]