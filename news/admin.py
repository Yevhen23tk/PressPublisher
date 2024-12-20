from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from news.models import Redactor, Newspaper, Topic


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
    )
    search_fields = ("username", "email", "first_name", "last_name")


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date")
    search_fields = ("title",)
    list_filter = ("published_date",)
    filter_horizontal = ("topics", "publishers")


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
