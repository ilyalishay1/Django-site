from django import forms
from django.forms import ModelForm
from .models import *


class AddPostForm(ModelForm):
    class Meta:
        model = PlayersModel
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 70, 'rows': 10}),
        }
