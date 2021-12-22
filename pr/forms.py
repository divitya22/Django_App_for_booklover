from django import forms
from django.forms import ModelForm
from .models import Trytab


class TrytabForm(ModelForm):
    class Meta:
        model=Trytab
        fields=('book_name','Type_book')
        # fields="__all__"

        labels = {
            'book_name':'',
            'Type_book':'',
        }

        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name of book'}),
            'Type_book': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What type of book is this??'}),
        }