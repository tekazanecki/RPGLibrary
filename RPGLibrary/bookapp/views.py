from rest_framework import generics,  viewsets
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import SettingForm, BookForm
from .models import Book, Setting
from .serializers import BookSerializer, SettingSerializer
from django.contrib.auth.decorators import login_required

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

class BooksBySettingView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        setting_id = self.kwargs['setting_id']
        return Book.objects.filter(setting_id=setting_id)


def index(request):
    return render(request, 'index.html')

@login_required
def root(request):
    settings = Setting.objects.all()
    return render(request, 'root.html', {'settings': settings})

@login_required
def books(request, setting_id):
    books = Book.objects.filter(setting_id=setting_id)
    return render(request, 'books.html', {'books': books, 'setting_id': setting_id})


@login_required
def new_setting(request):
    if request.method != 'POST':
        form = SettingForm()
    else:
        form = SettingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books:root'))

    contex = {'form': form}
    return render(request, 'new_setting.html', contex)

@login_required
def delete_setting(request, setting_id):
    setting = get_object_or_404(Setting, pk=setting_id)
    setting.delete()
    return redirect('books:root')

    return redirect('books:root')

@login_required
def new_book(request, setting_id):
    if request.method != 'POST':
        setting_default = Setting.objects.get(id=setting_id)
        form = BookForm(initial={'setting': setting_default})
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books:books', kwargs={'setting_id': setting_id}))

    contex = {'form': form, 'setting_id': setting_id}
    return render(request, 'new_book.html', contex)

@login_required
def delete_book(request, setting_id, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('books:books', setting_id=setting_id)

@login_required
def edit_setting(request, setting_id):
    setting = Setting.objects.get(id=setting_id)
    if request.method != 'POST':
        form = SettingForm(instance=setting)
    else:
        form = SettingForm(request.POST, instance=setting)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books:root'))

    context = {'form': form, 'setting_id': setting_id}
    return render(request, 'edit_setting.html', context)

@login_required
def edit_book(request, setting_id, book_id):
    book = Book.objects.get(id=book_id)
    if request.method != 'POST':
        form = BookForm(instance=book)
    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books:books', kwargs={'setting_id': setting_id}))

    context = {'form': form, 'setting_id': setting_id, 'book_id':book_id}
    return render(request, 'edit_book.html', context)