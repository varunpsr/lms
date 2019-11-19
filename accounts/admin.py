from django.contrib import admin
from .models import Librarian, Member

# Register your models here.

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ['user', 'library']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'city']
