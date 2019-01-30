from django.test import TestCase, Client
from django.urls import resolve, reverse
from lists.views import HomePage
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item



class ListsHome(TestCase):
    """
    Testing the Lists Home page/view 
    """
    def test_root_url_resloves_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, HomePage)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
  
        response = HomePage(request)
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string('lists/home.html',
                                         {'new_item_text': 'A new list item'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_POST_requests(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        
        new_item = Item.objects.first()
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(new_item.text, 'A new list item')

    def test_home_page_will_redirect_after_POST_requests(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = HomePage(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

class ItemModelTest(TestCase):
    
    def test_saving_and_retriving_models(self):
        first_item = Item()
        first_item.text = 'First Item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Second Item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_item_saved = saved_items[0]
        second_item_saved = saved_items[1]

        self.assertEqual(first_item_saved.text, first_item.text)
        self.assertEqual(second_item_saved.text, second_item.text)