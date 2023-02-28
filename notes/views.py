from django.shortcuts import render


def home(request):
    return render(request, 'notes/pages/home.html', context={
        'name': 'Enzo Belém Farias',
    })


def notes(request):
    return render(request, 'notes/pages/notes.html')
