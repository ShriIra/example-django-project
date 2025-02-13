from django.urls import path

from . import views

urlpatterns = [
    path("list", views.NotesListView.as_view(), name="notes.list"),
    path("popular", views.PopularNotesListView.as_view()),
    path("details/<int:pk>", views.NotesDetailView.as_view(), name="notes.detail"),
    path("new", views.NotesCreateView.as_view(), name="notes.new"),
    path("update/<int:pk>/edit", views.NotesUpdateView.as_view(), name="notes.update"),
    path("delete/<int:pk>", views.NotesDeleteView.as_view(), name="notes.delete"),
]