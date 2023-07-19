from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'users'

urlpatterns = [
    # strona logowania
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    # strona wylogowania
    path('logout', views.logout_view, name='logout'),
]