from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Note, Tag


def home(request):
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
