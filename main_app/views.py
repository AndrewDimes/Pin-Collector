from django.shortcuts import render
from .models import Pin

from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1> Hello </h1>')

def about(request):
  return render(request, 'about.html')

def pins_index(request):
  pins = Pin.objects.all()
  return render(request, 'pins/index.html', {'pins': pins})

def pins_detail(request, pin_id):
  pin = Pin.objects.get(id=pin_id)
  return render(request, 'pins/detail.html', { 'pin': pin})
  