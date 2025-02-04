from django.contrib import admin

from medical.models import Medical


@admin.register(Medical)
class MedicalAdmin(admin.ModelAdmin):
    list_display = ('title', 'information', 'price',)
    list_filter = ('title', 'price',)
    search_fields = ('title', 'price',)
