from django.contrib import admin

from .models import Sobre


class SobreAdmin(admin.ModelAdmin):
    list_display = ["title"]


admin.site.site_header = "Aillez Engenharia | Administração"
admin.site.site_title = "Aillez Engenharia"
admin.site.register(Sobre, SobreAdmin)