from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, SettingViewSet, index, \
    rpg_settings, new_setting, edit_setting, delete_setting, \
    books, new_book, edit_book, delete_book, \
    chapters, chapter, new_chapter, edit_chapter, delete_chapter


app_name = 'lib_app'

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'settings', SettingViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('settings/', rpg_settings, name='rpg_settings'),
    path('settings/new_setting', new_setting, name='new_rpg_setting'),
    path('settings/edit_setting/<int:rpg_setting_id>/', edit_setting, name='edit_rpg_setting'),
    path('settings/delete_setting/<int:rpg_setting_id>/', delete_setting, name='delete_rpg_setting'),
    path('settings/<int:rpg_setting_id>/books/', books, name='books'),
    path('settings/<int:rpg_setting_id>/books/new_book', new_book, name='new_book'),
    path('settings/<int:rpg_setting_id>/books/edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('settings/<int:rpg_setting_id>/books/delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('settings/<int:rpg_setting_id>/books/<int:book_id>/chapters', chapters, name='chapters'),
    path('settings/<int:rpg_setting_id>/books/<int:book_id>/chapters/<int:chapter_id>', chapter, name='chapter'),
    path('settings/<int:rpg_setting_id>/books/<int:book_id>/chapters/new_chapter', new_chapter, name='new_chapter'),
    path('settings/<int:rpg_setting_id>/books/<int:book_id>/chapters/edit_chapter/<int:chapter_id>', edit_chapter, name='edit_chapter'),
    path('settings/<int:rpg_setting_id>/books/<int:book_id>/chapters/delete_chapter/<int:chapter_id>', delete_chapter, name='delete_chapter'),
    path('lib/', include(router.urls)),
]
