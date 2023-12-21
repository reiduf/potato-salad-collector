from django.shortcuts import render
from .models import Potato

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def potatoes_index(request):
    potatoes = Potato.objects.all()
    return render(request, 'potatoes/index.html', {
        'potatoes': potatoes
    })