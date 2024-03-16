
from django.urls import path
from bookstore.views import *

urlpatterns = [
    path("home", homePage, name="home_page"),
    path("allbooks", allBooks, name="all_books"),
    path("allauthors", allAuthors, name="all_authors"),

    path('addbook', addBook, name='add_book'),
    path('books/<int:id>', getBook, name='get_book'),
    path('books/<int:id>/delete', deleteBook, name='delete_book'),
    path('books/<int:id>/edit', editBook, name='edit_book'),
    
    path('addauthor', addAuthor, name='add_author'),
    path('authors/<int:id>', getAuthor, name='get_author'),
    path('authors/<int:id>/delete', deleteAuthor, name='delete_author'),
    path('authors/<int:id>/edit', editAuthor, name='edit_author')
]
