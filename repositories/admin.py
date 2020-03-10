from django.contrib import admin

from .models import Repository

@admin.register(Repository)
class DependencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'updated_date']
