
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home2',views.home2,name="home2"),
    path('detail',views.detail,name="details"),
    path('detail2',views.to_web,name="details2"),
    path('add_data',views.add_data,name="add-data"),
    path('search_book',views.search_book,name="search-book"),
    path('book_list',views.book_list,name="book-list"),
    path('show_book/<book_id>',views.show_book,name='show-book'),
    path('book_text',views.book_text,name="book_text"),
    path('delete_book/<book_id>',views.delete_book,name='delete-book'),
    path('book_csv',views.book_csv,name="book_csv"),

]
