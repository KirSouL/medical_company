from django.contrib import admin

from staff.models import StaffMedical


@admin.register(StaffMedical)
class StaffMedicalAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'patronymic', 'last_name', 'position', 'experience',)
    list_filter = ('first_name', 'patronymic', 'last_name', 'position', 'experience',)
    search_fields = ('first_name', 'patronymic', 'last_name', 'position',)
