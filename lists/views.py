from django.shortcuts import render
from django.views.generic import TemplateView

def HomePage(request):
    return render(request, 'lists/home.html')

# Create your views here.
