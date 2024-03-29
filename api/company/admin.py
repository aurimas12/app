from django.contrib import admin
from api.company.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'logo_url')
    search_fields = ('name', 'city') 
    