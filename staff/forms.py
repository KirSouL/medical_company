from django import forms

from staff.models import StaffMedical


class MixinStyleForm:
    """ Класс примесь для стилизации форм """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StaffMedicalForm(MixinStyleForm, forms.ModelForm):
    class Meta:
        model = StaffMedical
        fields = '__all__'
