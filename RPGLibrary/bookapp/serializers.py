from rest_framework import serializers
from .models import Book, Setting

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'src_link', 'img_link', 'setting']

class SettingSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Setting
        fields = ['id', 'name', 'img_link', 'books']