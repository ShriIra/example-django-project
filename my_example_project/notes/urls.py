from django.urls import path

from . import views

urlpatterns = [
    path("list", views.NotesListView.as_view()),
    path("popular", views.PopularNotesView.as_view()),
    path("details/<int:pk>", views.NotesDetailView.as_view())
]