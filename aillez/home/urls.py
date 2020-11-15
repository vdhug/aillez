from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contato/", views.contato, name="contato"),
    path("estudos-de-caso/", views.estudos, name="estudos-de-caso")
]