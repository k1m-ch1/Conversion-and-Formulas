from django.shortcuts import render
from django.http import HttpResponse
import functools
from operator import add, mul
import math
# Create your views here.

class formula:
  def __init__(self, variables, modifier=lambda x: x):
    """
      Variables is a list and in that list contains a tuple of tuple.
      The first layer of tuple represents some variables that will add together.
      The second layer of tuple represents a fraction where the top is the nominator and the bottom is the denominator.
      The third layer of tuple represents tuples that will multiply it self.
      The fourth layer of tuple holds 2 info, ('name', 'unit'). Ex. ('radius', 'm')
      Ex.
    """
    self.variables = variables
    self.modifier = modifier
  
  def get_variables(self):
    """
      Get the name of all of the variables as a list of string.
    """
    ret_val = list()
    for i in self.variables:
      for j in i:
        if type(j) == tuple:
          for k in j:
            if type(k) == tuple:
              ret_val.append(k)
    return list(set(ret_val)) 
  
  def calculate(self, request):
    """
      request is a django class that contains information about the post request.
    """
    
    def get_val(formatted_tuple):
      """
        formatted_tuple is a tuple of size 2.
        ('name', 'unit')
        Ex.
        ('radius', 'm')
      """
      if type(formatted_tuple) == tuple: 
        return float(request.POST[formatted_tuple[0]])
      else:
        return formatted_tuple
    
    def evaluate_fraction(fraction):
      fraction = list(fraction)
      for i, tuple_to_num in enumerate(fraction):
        if type(tuple_to_num) == tuple:
          tuple_to_num = map(get_val, tuple_to_num)
          fraction[i] = functools.reduce(mul, tuple_to_num, 1)
      return float(fraction[0]/fraction[1]) 
    
    variables_temp = self.variables.copy()
    
    return self.modifier(functools.reduce(add, map(evaluate_fraction, variables_temp), 0)) 
      
      
      


type_of_formulas = ["area", "volume", "electricity", "kinematics", "thermodynamics"]
nav_in_type_of_formulas = {
  "area":["square", "rectangle", "right triangle", "circle"],
  "volume":["cube", "cuboid", "cylinder", "cone", "sphere"],
  "electricity":["resistance", "current", "voltage", "capacitance"],
  "kinematics":["velocity", "acceleration"],
  "thermodynamics":["heat"]
  }
BASE = ('base', 'm')
LENGTH = ('length', 'm')
HEIGHT = ('height', 'm')
RADIUS = ('radius', 'm')
RESISTIVITY = ('resistivity', 'ohm*m')
CHARGE = ('charge', 'C')
CURRENT = ('current', 'A')
CAPACITANCE = ('capacitance', 'F')
DISTANCE = ('distance', 'm')
TIME = ('time', 's')
HEAT = ('heat', 'J')
ACCELERATION = ('acceleration', 'ms^(-2)')
VELOCITY = ('velocity', 'ms^(-1)')
HEAT_CAPACITY = ('heat capacity', 'J(mk)^(-1)')
VOLTAGE = ('voltage', 'V')
AREA = ('area', 'm^2')
RESISTANCE = ('resistance', 'ohm')
TEMPERATURE = ('temperature', 'k')
MASS = ('mass', 'kg')

formulas = {'square': formula([((LENGTH, LENGTH), 1)]), 
            'rectangle': formula([((LENGTH, HEIGHT),1)]), 
            'right triangle': formula([((BASE, BASE),1), ((HEIGHT, HEIGHT),1)], math.sqrt),
            'circle': formula([((math.pi, RADIUS, RADIUS), 1)]), 
            'cube': formula([((LENGTH, LENGTH, LENGTH),1)]),
            'cuboid': formula([((LENGTH, BASE, HEIGHT),1)]), 
            'cylinder': formula([((math.pi, RADIUS, RADIUS, HEIGHT), 1)]), 
            'cone': formula([((1/3,RADIUS, RADIUS, math.pi),1)]), 
            'sphere': formula([((4/3, RADIUS, RADIUS, RADIUS, math.pi),1)]), 
            'resistance': formula([((RESISTIVITY, LENGTH), (AREA,))]), 
            'current': formula([((CHARGE,),(TIME,))]), 
            'voltage': formula([((CURRENT, RESISTANCE), 1)]), 
            'capacitance': formula([((CHARGE,VOLTAGE),1)]), 
            'velocity': formula([((DISTANCE,),(TIME,))]), 
            'acceleration': formula([((VELOCITY,),(TIME,))]), 
            'heat': formula([((MASS, HEAT_CAPACITY, TEMPERATURE),1)])}


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
  return render(request, 'home/nav_layout.html', {
    "name_app":"formulas",
    "classification": "Type of formulas",
    "nav_name": zip(nav_in_type_of_formulas[type], map(capitalize, nav_in_type_of_formulas[type])),
    "title" : "Type of formulas",
    "heading": "Formulas"
  })

def handle_formula(request, formula_type, formula):
  dict_to_send = {
    "name_app":"formulas",
    "classification": formula.capitalize(),
    "nav_name": formulas[formula].get_variables(),
    "title" : formula.capitalize(),
    "heading": "Formulas", 
    "result":None,
  }
  if request.method == "POST":  dict_to_send["result"] = formulas[formula].calculate(request)
  return render(request, 'formulas/formula.html', dict_to_send)