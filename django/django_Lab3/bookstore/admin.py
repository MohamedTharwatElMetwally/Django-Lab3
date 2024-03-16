from django.contrib import admin

# Register your models here.

from bookstore.models import BookModel, AuthorModel

admin.site.register(BookModel)
admin.site.register(AuthorModel)