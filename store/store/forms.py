from django import forms
from images.models import DocModel

class DocForm(forms.ModelForm):
    class Meta:
        model = DocModel
        fields = ['name', 'doc']
