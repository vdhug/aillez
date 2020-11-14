from django import forms
from django.db import models
from django.contrib import admin

from .models import SobreNos, Compromisso


class SobreNosAdmin(admin.ModelAdmin):
    list_display = ["title"]

# class GroupAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]
#     exclude = ('members',)

admin.site.site_header = "Aillez Engenharia | Administração"
admin.site.site_title = "Aillez Engenharia"
admin.site.register(SobreNos, SobreNosAdmin)
# admin.site.register(Compromisso, CompromissoAdmin)