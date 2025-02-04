from django import forms
from django.forms import BooleanField

from medical.models import Medical


class MixinStyleForm:
    """ Класс примесь для стилизации форм """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class MedicalForm(MixinStyleForm, forms.ModelForm):
    class Meta:
        model = Medical
        fields = '__all__'
