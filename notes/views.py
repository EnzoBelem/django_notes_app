from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Note, Tag


def home_page(request):
    notes = Note.objects.filter(is_published=True).order_by('-id')
    return render(request, 'notes/pages/home.html', context={
        'notes': notes,
        'title': 'Home'
    })


def tag_page(request, tag_id):
    notes = get_list_or_404(
        Note.objects.filter(
            is_published=True,
            tags__id=tag_id
        ).order_by('-id')
    )
    tag_name = get_object_or_404(Tag, id=tag_id).name

    return render(request, 'notes/pages/home.html', context={
        'notes': notes,
        'title': f'Tag - {tag_name}'
    })


def note_details(request, note_id):
    note = get_object_or_404(
        Note.objects.filter(
            id=note_id
        ).order_by('-id')
    )
    return render(request, 'notes/pages/note_page.html', context={
        'note': note,
    })


def note_search(request):

    search_query = request.GET.get('q', '').strip()

    if not search_query:
        return HttpResponse(status=404)

    return render(request, 'notes/pages/search_page.html',
                  context={'title': 'Search',
                           'search_query': search_query})
