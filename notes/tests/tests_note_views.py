from django.test import TestCase
from django.urls import resolve, reverse

from notes import views


class Note_views_test(TestCase):
    def test_notes_home_view_function_is_correct(self):
        view = resolve(reverse('notes:home'))
        self.assertIs(view.func, views.home)

    def test_notes_note_page_view_function_is_correct(self):
        view = resolve(reverse(viewname='notes:note_page', args=[1]))
        self.assertIs(view.func, views.note)

    def test_notes_note_page_tag_view_function_is_correct(self):
        view = resolve(
            reverse(viewname='notes:tag_page', kwargs={'tag_id': 3}))
        self.assertIs(view.func, views.notes_by_tag)
