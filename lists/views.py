from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from lists.models import Item

def HomePage(request):
    if request.method == 'POST':
        item_text = request.POST.get('item_text', '')
        item = Item(text=item_text)
        item.save()
        return redirect('/')
        
    return render(request, 'lists/home.html',{
        'new_item_text': request.POST.get('item_text', 'A new list item'),
    })

# Create your views here.
