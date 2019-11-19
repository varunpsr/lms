from django.contrib import admin
from django import forms
from .models import Book, Author, Publication, LibraryBooks, IssuedBook, Language

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'publication', 'price', 'language', 'isbn']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(LibraryBooks)
class LibraryBooksAdmin(admin.ModelAdmin):
    list_display = ['library', 'book', 'status']

@admin.register(IssuedBook)
class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ['member', 'book', 'date_of_issue', 'date_of_return', 'actual_date_of_return', 'librarian', 'library']

admin.site.register(Language)