from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "rating")
    list_filter = ("author", "rating")
admin.site.register(Book, BookAdmin)