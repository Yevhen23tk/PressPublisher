from django.contrib import admin
from django.urls import path

from news.views import index, NewspaperListView, NewspaperDetailView, NewspaperCreateView

urlpatterns = [
    path('', index, name='index'),
    path('newspapers/', NewspaperListView.as_view(), name='newspaper-list'),
    path('newspapers/<int:pk>/', NewspaperDetailView.as_view(), name='newspaper-detail'),
    path('newspapers/create/', NewspaperCreateView.as_view(), name='newspaper-create'),
]

app_name = "news"
