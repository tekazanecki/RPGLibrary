from django import forms
from .models import RPGSetting, Book, Chapter

class SettingForm(forms.ModelForm):
    class Meta:
        model = RPGSetting
        fields = ['name','image']
        labels = {
            'name': 'Setting Name',
            'image': 'Image',
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','image', 'pdf', 'rpg_setting']
        labels = {
            'title': 'Book Title',
            'image': 'Book Image',
            'pdf': 'Book PDF',
            'rpg_setting': 'RPG Setting'
        }

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'short_description', 'content', 'book']
        labels = {
            'title': 'Chapter Title',
            'content': 'Chapter Content',
            'book': "Book"
        }