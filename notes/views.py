from django.shortcuts import render

from utils.notes.factory import make_note


def home(request):
    return render(request, 'notes/pages/home.html', context={
        'notes': [make_note() for _ in range(10)],
    })


def note(request, note_id):
    return render(request, 'notes/pages/note_page.html', context={
        'note': make_note(),
    })
