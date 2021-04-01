from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic import ListView, DetailView
from .models import Pin, Category
from .forms import CommentForm

from django.http import HttpResponse

class PinCreate(CreateView):
  model = Pin
  fields = '__all__'

class PinUpdate(UpdateView):
  model = Pin
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['description', 'price']

class PinDelete(DeleteView):
  model = Pin
  success_url = '/pins/'

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pins_index(request):
  pins = Pin.objects.all()
  return render(request, 'pins/index.html', {'pins': pins})

def pins_detail(request, pin_id):
  pin = Pin.objects.get(id=pin_id)
  comment_form = CommentForm()
  return render(request, 'pins/detail.html', { 'pin': pin, 'comment_form': comment_form})
  
def add_comment(request, pin_id):
  form = CommentForm(request.POST)

  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.pin_id = pin_id
    new_comment.save()
  return redirect('detail', pin_id=pin_id)

class CategoryList(ListView):
  model = Category

def categories_detail(request, category_id):
  category = Category.objects.get(id=category_id)
  pins_cat_doesnt_have = Pin.objects.exclude(id__in = category.pins.all().values_list('id'))
  return render(request, 'categories/detail.html', { 'category': category, 'pins' : pins_cat_doesnt_have})

def assoc_pin(request, category_id, pin_id):
  # Note that you can pass a toy's id instead of the whole object
  category = Category.objects.get(id=category_id)
  pin = Pin.objects.get(id=pin_id)
  category.pins.add(pin)
  return redirect('categories_detail', category_id=category_id)

class CategoryCreate(CreateView):
  model = Category
  fields = ['name', 'description']

class CategoryUpdate(UpdateView):
  model = Category
  fields = ['name', 'description']

class CategoryDelete(DeleteView):
  model = Category
  success_url = '/categories/'