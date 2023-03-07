from django.urls import path

from notes.views import home, note

app_name = 'notes'

urlpatterns = [
    path('', home, name='home'),
    path('notes/<int:note_id>', note, name='note_page')
]
