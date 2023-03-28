from django.test import TestCase
from django.urls import resolve, reverse

from notes import views


class Note_views_test(TestCase):
    def test_notes_home_page_view_function_is_correct(self):
        view = resolve(reverse('notes:home_page'))
        self.assertIs(view.func, views.home_page)

    def test_notes_note_details_view_function_is_correct(self):
        view = resolve(reverse(viewname='notes:note_details', args=[1]))
        self.assertIs(view.func, views.note_details)

    def test_notes_tag_page_view_function_is_correct(self):
        view = resolve(
            reverse(viewname='notes:tag_page', kwargs={'tag_id': 3}))
        self.assertIs(view.func, views.tag_page)

    def test_notes_note_search_view_function_is_correct(self):
        view = resolve(reverse(viewname='notes:note_search'))
        self.assertIs(view.func, views.note_search)

    def test_notes_note_search_view_loads_correct_template(self):
        response = self.client.get(reverse('notes:note_search')+'?q=teste')
        self.assertTemplateUsed(response, 'notes/pages/search_page.html')

    def test_notes_note_search_raise_404_if_no_search_term(self):
        response = self.client.get(reverse(viewname='notes:note_search'))
        self.assertEqual(response.status_code, 404)
