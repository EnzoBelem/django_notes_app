from django.shortcuts import render


def home(request):
    return render(request, 'notes/pages/home.html', context={
        'name': 'Enzo Belém Farias', 'note': 1, 'number_of_notes': [1, 2, 3]
    })


def note(request, note_id):
    return render(request, 'notes/pages/note_view.html', context={
        'note_id': note_id
    })
