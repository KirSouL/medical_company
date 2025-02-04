from django.urls import path
from django.views.decorators.cache import cache_page

from medical.apps import MedicalConfig
from medical.views import MedicalCreateView, MedicalUpdateView, MedicalDetailView, MedicalListView, MedicalDeleteView, \
    ContactsView, CompanyView

app_name = MedicalConfig.name

urlpatterns = [
    path('medical/create/', MedicalCreateView.as_view(), name='medical-create'),
    path('medical/update/<int:pk>', MedicalUpdateView.as_view(), name='medical-update'),
    path('medical/detail/<int:pk>', MedicalDetailView.as_view(), name='medical-detail'),
    path('medical/list/', cache_page(60)(MedicalListView.as_view()), name='medical-list'),
    path('medical/delete/<int:pk>', MedicalDeleteView.as_view(), name='medical-delete'),
    path('medical/contacts/', ContactsView.as_view(), name='contacts'),
    path('medical/company/', CompanyView.as_view(), name='company'),
]
