from django.test import TestCase, Client
from django.urls import resolve, reverse
from lists.views import HomePage
from django.http import HttpRequest

clinet = Client()

class ListsHome(TestCase):
    def test_root_url_resloves_home_page_view(self):
        found = resolve('/')
        print(found.func, HomePage)
        self.assertEqual(found.func, HomePage) 
    
    def test_home_page_returns_correct_html(self):
        response = clinet.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>To-Do</title>', response.content)      
        self.assertTrue(response.content.endswith(b'</html>'))  
# Create your tests here.

