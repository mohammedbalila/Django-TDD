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
        
    items = Item.objects.all()
    # print(items[0].id)
    return render(request, 'lists/home.html', {'items': items})

# Create your views here.
