from django.test import TestCase, Client
from django.urls import resolve, reverse
from lists.views import HomePage
from django.http import HttpRequest
from django.template.loader import render_to_string

clinet = Client()

class ListsHome(TestCase):
    def test_root_url_resloves_home_page_view(self):
        found = resolve('/')
        print(found.func, HomePage)
        self.assertEqual(found.func, HomePage) 
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        # response = clinet.get('/')
        response = HomePage(request)
        expected_html = render_to_string('lists/home.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), expected_html)  
# Create your tests here.

