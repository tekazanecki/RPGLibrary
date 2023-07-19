from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets, generics

from .forms import SettingForm, BookForm, ChapterForm
from .models import Chapter, Book, RPGSetting
from .serializers import ChapterSerializer, BookSerializer, SettingSerializer
from django.contrib.auth.decorators import login_required


# REST API
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SettingViewSet(viewsets.ModelViewSet):
    queryset = RPGSetting.objects.all()
    serializer_class = SettingSerializer

class BooksBySettingView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        setting_id = self.kwargs['rpg_setting_id']
        return Book.objects.filter(rpg_setting_id=setting_id)

class ChapterByBookView(generics.ListAPIView):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Chapter.objects.filter(book_id=book_id)


# function VIEWs
def index(request):
    return render(request, 'index.html')


# SETTINGS
@login_required
def rpg_settings(request):
    rpg_settings = RPGSetting.objects.all()
    return render(request, 'rpg_settings.html', {'rpg_settings': rpg_settings})

@login_required
def new_setting(request):
    if request.method != 'POST':
        form = SettingForm()
    else:
        form = SettingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lib_app:rpg_settings'))

    contex = {'form': form}
    return render(request, 'rpg_setting_new.html', contex)

@login_required
def delete_setting(request, rpg_setting_id):
    setting = get_object_or_404(RPGSetting, pk=rpg_setting_id)
    setting.delete()
    return redirect('lib_app:rpg_settings')

@login_required
def edit_setting(request, rpg_setting_id):
    setting = RPGSetting.objects.get(id=rpg_setting_id)
    if request.method != 'POST':
        form = SettingForm(instance=setting)
    else:
        form = SettingForm(request.POST, request.FILES,  instance=setting)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lib_app:rpg_settings'))

    context = {'form': form, 'rpg_setting_id': rpg_setting_id}
    return render(request, 'rpg_setting_edit.html', context)


# BOOKS
@login_required
def books(request, rpg_setting_id):
    books = Book.objects.filter(rpg_setting_id=rpg_setting_id)
    return render(request, 'books.html', {'books': books, 'rpg_setting_id': rpg_setting_id})


@login_required
def new_book(request, rpg_setting_id):
    if request.method != 'POST':
        setting_default = RPGSetting.objects.get(id=rpg_setting_id)
        form = BookForm(initial={'setting': setting_default})
    else:
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lib_app:books', kwargs={'rpg_setting_id': rpg_setting_id}))

    contex = {'form': form, 'rpg_setting_id': rpg_setting_id}
    return render(request, 'book_new.html', contex)

@login_required
def delete_book(request, rpg_setting_id, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('lib_app:books', rpg_setting_id=rpg_setting_id)

@login_required
def edit_book(request, rpg_setting_id, book_id):
    book = Book.objects.get(id=book_id)
    if request.method != 'POST':
        form = BookForm(instance=book)
    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lib_app:books', kwargs={'rpg_setting_id': rpg_setting_id}))

    context = {'form': form, 'rpg_setting_id': rpg_setting_id, 'book_id': book_id}
    return render(request, 'book_edit.html', context)

# CHAPTERS

def chapter(request, rpg_setting_id, book_id, chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    return render(request, 'chapter.html', {'chapter': chapter, 'rpg_setting_id': rpg_setting_id,'book_id': book_id})

def chapters(request, rpg_setting_id, book_id):
    chapters = Chapter.objects.filter(book_id=book_id)
    return render(request, 'chapters.html', {'chapters': chapters, 'rpg_setting_id': rpg_setting_id,'book_id': book_id})

def new_chapter(request, rpg_setting_id, book_id):
    if request.method != 'POST':
        form = ChapterForm()
    else:
        form = ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lib_app:chapters', kwargs={'book_id': book_id, 'rpg_setting_id': rpg_setting_id}))

    contex = {'form': form, 'rpg_setting_id': rpg_setting_id,'book_id': book_id}
    return render(request, 'chapter_new.html', contex)

def delete_chapter(request, rpg_setting_id, book_id, chapter_id):
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    chapter.delete()
    return redirect('lib_app:chapters', rpg_setting_id=rpg_setting_id, book_id=book_id)


def edit_chapter(request, rpg_setting_id, book_id, chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    if request.method != 'POST':
        form = ChapterForm(instance=chapter)
    else:
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lib_app:chapters', kwargs={'book_id': book_id, 'rpg_setting_id': rpg_setting_id}))

    context = {'form': form, 'rpg_setting_id': rpg_setting_id, 'book_id': book_id, 'chapter_id': chapter_id}
    return render(request, 'chapter_edit.html', context)

