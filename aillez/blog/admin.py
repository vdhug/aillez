from .models import Estudo
from django.contrib import admin

# Register your models here.
class EstudoAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


admin.site.site_header = "Aillez Engenharia | Administração"
admin.site.site_title = "Aillez Engenharia"
admin.site.register(Estudo, EstudoAdmin)