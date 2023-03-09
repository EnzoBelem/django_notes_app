from django.shortcuts import render

from .models import Note

# from utils.notes.factory import make_note


def home(request):
    notes = Note.objects.filter(is_published=True).order_by('-id')
    return render(request, 'notes/pages/home.html', context={
        'notes': notes,
    })


def notes_by_tag(request, tag_id):
    notes = Note.objects.filter(
        is_published=True, tags__id=tag_id).order_by('-id')
    return render(request, 'notes/pages/home.html', context={
        'notes': notes,
    })


def note(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'notes/pages/note_page.html', context={
        'note': note,
    })
