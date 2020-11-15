from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Servico


class ServicoAdmin(admin.ModelAdmin):
    # list_display = ["title"]
    pass


admin.site.site_header = "Aillez Engenharia | Administração"
admin.site.site_title = "Aillez Engenharia"
admin.site.register(Servico, ServicoAdmin)