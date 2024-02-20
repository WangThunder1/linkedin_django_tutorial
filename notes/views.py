# pylint: disable=no-member,redefine-builtin,
from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView
from .models import Notes

# Create your views here.
class NotesListView(ListView):
    model = Notes
    context_object_name ="notes"
    template_name ="notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name ="note"


