from django import forms
from .models import Register_model


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register_model
        fields = '__all__'
