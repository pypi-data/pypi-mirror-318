
from django.contrib import admin

from .models import Something


@admin.register(Something)
class SomethingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('name',)
