from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView, DeleteView, ListView, DetailView

from medical.forms import MedicalForm
from medical.models import Medical
from medical.services import get_medicals


class MedicalCreateView(CreateView):
    model = Medical
    form_class = MedicalForm
    success_url = reverse_lazy('medical:medical_list')


class MedicalUpdateView(UpdateView):
    model = Medical
    form_class = MedicalForm

    def get_success_url(self):
        return reverse('medical:view', args=[self.kwargs.get('pk')])


class MedicalDeleteView(DeleteView):
    model = Medical
    success_url = reverse_lazy('medical:medical_list')


class MedicalDetailView(DetailView):
    model = Medical


class MedicalListView(ListView):
    model = Medical

    def get_queryset(self):
        return get_medicals()


class ContactsView(TemplateView):
    template_name = "medical/contacts.html"


class CompanyView(TemplateView):
    template_name = "medical/company.html"
