from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pin

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
  return render(request, 'pins/detail.html', { 'pin': pin})
  