from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, SettingViewSet, index, root, books, \
    new_setting, edit_setting, delete_setting, \
    new_book, edit_book, delete_book

app_name = 'books'

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'settings', SettingViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('root/', root, name='root'),
    path('root/new_setting', new_setting, name='new_setting'),
    path('root/edit_setting/<int:setting_id>/', edit_setting, name='edit_setting'),
    path('root/delete_setting/<int:setting_id>/', delete_setting, name='delete_setting'),
    path('settings/<int:setting_id>/books/', books, name='books'),
    path('settings/<int:setting_id>/books/new_book', new_book, name='new_book'),
    path('settings/<int:setting_id>/books/edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('settings/<int:setting_id>/books/delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('lib/', include(router.urls)),
]
