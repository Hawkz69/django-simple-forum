from django.contrib import admin
from .models import Curse

class CurseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date']
    search_fields = ['name']

admin.site.register(Curse, CurseAdmin)
