# from django import forms
from django.contrib import admin
# from django.utils.safestring import mark_safe
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
# from modeltranslation.admin import TranslationAdmin

from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")


# admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
