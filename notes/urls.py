from django.urls import path

from notes import views

app_name = 'notes'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('notes/search/', views.note_search, name='note_search'),
    path('notes/tags/<int:tag_id>', views.tag_page, name='tag_page'),
    path('notes/details/<int:note_id>', views.note_details,
         name='note_details'),
]
