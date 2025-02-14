from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import NotesForm
from .models import Notes

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, "notes/notes_list.html", {"notes": all_notes})

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"

# def details(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Notes does not exist")
    
#     return render(request, "notes/notes_detail.html", {"note": note})

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

class PopularNotesView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    queryset = Notes.objects.filter(likes__gte=1)

class NotesCreateView(CreateView):
    # model = Notes
    # fields = ['title', 'text']
    success_url = "/notes/list"
    template_name = "notes/notes_form.html"
    form_class = NotesForm

class NotesUpdateView(UpdateView):
    model = Notes
    # fields = ['title', 'text']
    success_url = '/notes/list'
    template_name = "notes/notes_edit_form.html"
    form_class = NotesForm
    context_object_name = "note"

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/notes/list'
    template_name = "notes/notes_confirm_delete.html"
    context_object_name = "note"
