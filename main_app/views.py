from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

def potatoes_detail(request, potato_id):
    potato = Potato.objects.get(id=potato_id)
    return render(request, 'potatoes/detail.html', {
        'potato': potato
    })

class PotatoCreate(CreateView):
    model = Potato
    fields = '__all__'

class PotatoUpdate(UpdateView):
    model = Potato
    fields = '__all__'

class PotatoDelete(DeleteView):
    model = Potato
    success_url = '/potatoes'