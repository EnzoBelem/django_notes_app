from django.urls import path

from notes.views import home, note, notes_by_tag

app_name = 'notes'

urlpatterns = [
    path('', home, name='home'),
    path('notes/tags/<int:tag_id>', notes_by_tag, name='tag_page'),
    path('notes/<int:note_id>', note, name='note_page'),

]
