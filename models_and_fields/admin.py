from django.contrib import admin
from models_and_fields import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name']


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.BookReviewer)
class BookReviewerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(models.Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote']


@admin.register(models.AboutGenre)
class AboutGenreAdmin(admin.ModelAdmin):
    pass