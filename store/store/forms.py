from django import forms
from stores.models import DocModel

class DocForm(forms.ModelForm):
    class Meta:
        model = DocModel
        fields = ['name', 'doc']
