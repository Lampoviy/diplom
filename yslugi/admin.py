from django.contrib import admin
from yslugi.models import Yslugi

@admin.register(Yslugi)
class YslugiAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
