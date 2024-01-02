from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Potato
from .forms import CommentForm

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
    comment_form = CommentForm()
    return render(request, 'potatoes/detail.html', {
        'potato': potato,
        'comment_form': comment_form
    })

def add_comment(request, potato_id):
  pass 

def add_comment(request, potato_id):
  form = CommentForm(request.POST)

  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.potato_id = potato_id
    new_comment.save()
  return redirect('detail', potato_id=potato_id)

class PotatoCreate(CreateView):
    model = Potato
    fields = '__all__'

class PotatoUpdate(UpdateView):
    model = Potato
    fields = '__all__'

class PotatoDelete(DeleteView):
    model = Potato
    success_url = '/potatoes'