from django import forms
from .models import Setting, Book

class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ['name','img_link']
        labels = {
            'name': 'Setting Name',
            'img_link': 'Setting Image Link',
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','src_link', 'img_link', 'setting']
        labels = {
            'title': 'Book Title',
            'src_link': 'Book Source Link',
            'img_link': 'Book Image Link',
            'setting': 'Book Setting'
        }