from django.shortcuts import render
from django.http import Http404

from django.views.generic import ListView, DetailView

from .models import Notes


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    # template_name = "notes/custom_notes_list.html"


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, "notes/notes_list.html", {"notes": all_notes})

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_details.html"


# def details(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, "notes/notes_details.html", {"note": note})

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    queryset = Notes.objects.filter(likes__gte=1)