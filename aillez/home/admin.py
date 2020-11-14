from django.contrib import admin

from .models import PaginaHome


class PaginaHomeAdmin(admin.ModelAdmin):
    exclude = (["title"])
    fields = ["slogan", "sobre_titulo", "sobre_descricao", "sobre_time"]
    list_display = (["title"])

admin.site.site_header = "Aillez Engenharia | Administração"
admin.site.site_title = "Aillez Engenharia"
admin.site.register(PaginaHome, PaginaHomeAdmin)
