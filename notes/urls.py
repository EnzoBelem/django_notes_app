from django.urls import path

from notes.views import home

urlpatterns = [
    path('', home)
]
