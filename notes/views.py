from django.shortcuts import render


def home(request):
    return render(request, 'notes/home.html', context={
        'name': 'Enzo Belém Farias',
    })
