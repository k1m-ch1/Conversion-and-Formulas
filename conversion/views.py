from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

type_of_units = ["length", "area", "volume", "temperature"]

def index(request):
  return render(request, 'home/nav_layout.html',{
    "classification":"Type of units", 
    "name_app": "conversion",
    "nav_name": zip(type_of_units, map(lambda x: x.capitalize(), type_of_units)),
    "title": "Unit Types",
    "heading": "Unit Types"
  })
  
def length(request):
  return render(request, 'conversion/length.html')

def area(request):
  return render(request, 'conversion/area.html')

def volume(request):
  return render(request, 'conversion/volume.html')

def temperature(request):
  return render(request, 'conversion/temperature.html')

def handle_type(request, type):
  return HttpResponse(f"Good morning! {type}")