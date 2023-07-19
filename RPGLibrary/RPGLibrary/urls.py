from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('userapp.urls', namespace='users')),
    path('', include('bookapp.urls', namespace='books')),
]