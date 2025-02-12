from django.urls import path

from . import views

urlpatterns = [
    path("list", views.NotesListView.as_view(), name="notes.list"),
    path("popular", views.PopularNotesView.as_view(), name="notes.popular"),
    path("details/<int:pk>", views.NotesDetailView.as_view(), name="notes.detail"),
    path("new", views.NotesCreateView.as_view(), name="notes.new")
]