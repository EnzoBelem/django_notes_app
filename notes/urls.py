from django.urls import path

from notes.views import home, note_details, tag_page

app_name = 'notes'

urlpatterns = [
    path('', home, name='home'),
    path('notes/tags/<int:tag_id>', tag_page, name='tag_page'),
    path('notes/details/<int:note_id>', note_details, name='note_details'),

]
