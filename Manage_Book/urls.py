from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage_book, name='home'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:id>/', views.edit_book, name='edit_book'),
    path('update_book/<int:id>/', views.update_book, name='update_book'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
    path('delete_all/', views.delete_all, name='delete_all'),
]
