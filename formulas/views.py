from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

type_of_formulas = ["area", "volume", "electricity", "kinematics", "thermodynamics"]

def capitalize(str):
  return str.capitalize()

def index(request):
  return render(request, 'home/nav_layout.html', {
    "name_app":"formulas",
    "classification": "Type of formulas",
    "nav_name": zip(type_of_formulas, map(capitalize, type_of_formulas)),
    "title" : "Type of formulas",
    "heading": "Formulas"
  })

def handle_type(request, type):
  return HttpResponse(f"Hello, {type}!")