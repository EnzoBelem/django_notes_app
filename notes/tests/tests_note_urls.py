from django.test import TestCase
from django.urls import reverse


class Note_url_test(TestCase):
    def test_notes_home_url_is_correct(self):
        home_url = reverse('notes:home_page')
        self.assertEqual(home_url, '/')

    def test_notes_note_page_tag_url_is_correct(self):
        note_tag_url = reverse(viewname='notes:tag_page', args=[3])
        self.assertEqual(note_tag_url, '/notes/tags/3')

    def test_notes_note_page_url_is_correct(self):
        note_page_url = reverse(viewname='notes:note_details', args=[1])
        self.assertEqual(note_page_url, '/notes/details/1')

    def test_notes_note_search_url_is_correct(self):
        note_search_url = reverse(viewname='notes:note_search')
        self.assertEqual(note_search_url, '/notes/search/')
