from django import forms
from .models import Rap

class RapForm(forms.ModelForm):
    class Meta:
        model = Rap
        fields = ['title', 'text', 'tags']
        labels = {'title':'Titulo', 'text':'Letra'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}



