from rest_framework import serializers
from .models import Chapter, Book, RPGSetting

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'title', 'content', 'book']

class BookSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'image', 'pdf', 'setting', 'chapters']

class SettingSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = RPGSetting
        fields = ['id', 'name', 'image', 'books']
