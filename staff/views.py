from django.views.generic import ListView, DetailView

from staff.models import StaffMedical
from staff.services import get_staffs


class StaffMedicalDetailView(DetailView):
    model = StaffMedical


class StaffMedicalListView(ListView):
    model = StaffMedical

    def get_queryset(self):
        return get_staffs()
