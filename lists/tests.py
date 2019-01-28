from django.test import TestCase
from django.urls import resolve
from lists.views import HomePage

class ListsHome(TestCase):
    def test_root_url_resloves_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, HomePage) 
# Create your tests here.
