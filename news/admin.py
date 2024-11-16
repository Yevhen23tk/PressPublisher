from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from news.models import Redactor, Newspaper, Topic


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',)
    search_fields = ('username', 'email', 'first_name', 'last_name')


# Register the Newspaper model
@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')  # Make sure these fields exist in the Newspaper model
    search_fields = ('title',)
    list_filter = ('published_date',)
    filter_horizontal = ('topics', 'publishers')  # For ManyToMany fields


# Register the Topic model
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)  # The "Topic" model has a "name" field
    search_fields = ('name',)
