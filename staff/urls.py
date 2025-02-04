from django.urls import path
from django.views.decorators.cache import cache_page

from staff.apps import StaffConfig
from staff.views import (
    StaffMedicalDetailView,
    StaffMedicalListView
                         )

app_name = StaffConfig.name

urlpatterns = [
    path('staff/detail/<int:pk>', StaffMedicalDetailView.as_view(), name='staff-detail'),
    path('staff/list/', cache_page(60)(StaffMedicalListView.as_view()), name='staff-list'),
]
