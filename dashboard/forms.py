from django import forms
from .models import quer

class queryform(forms.ModelForm):
    class Meta:
        model = quer
        fields = '__all__'
