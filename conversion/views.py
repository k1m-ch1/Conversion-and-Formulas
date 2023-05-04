from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Unit:
  useless_func = lambda x: x
  # base_type = {"length": unit('meter', 'm', "length"),
  #              "area": unit('meter squared', 'm^2', "area"),
  #              "volume": unit('meter cubed', 'm^3', "volume"),
  #              "temperature": unit('degree celcius', '℃', "temperature")}
  # type_of_units = base_type.keys()
  def __init__(self, unit_name, unit_abbr, cvt_to_base=useless_func, cvt_to_unit=useless_func):
    self.unit_name = unit_name
    self.unit_abbr = unit_abbr
    self.cvt_to_base = cvt_to_base
    self.cvt_to_unit = cvt_to_unit
    # self.unit_type = unit_type
    
  get_name_and_abbr = lambda self: (self.unit_name, self.unit_abbr)
  
  def cvt(self, input_data, output_unit):
    """Convert from one unit to the other
    Args:
        input_data: float
        output_unit (Unit): is of class Unit

    Returns:
        converted_data, (output_unit_name, output_unit_abbreviation): _description_
    """
    return input_data, output_unit.cvt_to_unit(self.cvt_to_base(input_data)), self.get_name_and_abbr(), output_unit.get_name_and_abbr()

UNIT_DATA = {
    "length":[
    Unit("meter", "m", Unit.useless_func, Unit.useless_func),
    Unit("kilometer", "km", lambda x: x*(10**3), lambda x: x/(10**3)),
    Unit("decimeter", "dm", lambda x: x/10, lambda x: x*10),
    Unit("centimeter", "cm", lambda x: x/(10**2), lambda x: x*(10**2)),
    Unit("yard", "yd", lambda x: x*0.9144, lambda x: x/0.9144),
    Unit("feet", "ft", lambda x: x*0.3048, lambda x: x/0.3048),
    Unit("inch", "in", lambda x: x*0.0254, lambda x: x/0.0254),
    Unit("milimeter", "mm", lambda x: x/(10**3), lambda x: x*(10**3)),
    Unit("mile", "mi", lambda x: x*1609.34, lambda x: x/1609.34)], 
  "area":[
    Unit("square meter", "m^2", Unit.useless_func, Unit.useless_func),
    Unit("square kilometer", "km^2", lambda x: x*(10**6), lambda x: x/(10**6)),
    Unit("hectar", "ha", lambda x: x*(10**4), lambda x: x/(10**4)),
    Unit("acre", "arce", lambda x: x*4046.86, lambda x: x/4046.86),
    Unit("square mile", "mi^2", lambda x: x*2.59*(10**6), lambda x: x/(2.59*(10**6))),
    Unit("square yard", "yr^2", lambda x: x*0.836127, lambda x: x/0.836127)],
  "volume":[
    Unit("liter", "l", Unit.useless_func, Unit.useless_func),
    Unit("cubic meter", "m^3", lambda x: x*(10**3), lambda x: x/(10**3)),
    Unit("US gallon", "US gal", lambda x: x*(3.78541), lambda x: x/(3.78541)), 
    Unit("US quart", "US quart", lambda x: x*(0.946353), lambda x: x/0.946353),
    Unit("US pint", "US pint", lambda x: x*(0.473176), lambda x: x/(0.473176)),
    Unit("US tablespoon", "US tbs", lambda x: x*(0.0147868), lambda x: x/0.0147868),
    Unit("US teaspoon", "US ts", lambda x: x*0.00492892, lambda x: x/0.00492892),
    Unit("fluid ounce", "oz", lambda x: x*0.0295735, lambda x: x/0.0295735),
    Unit("Imperial tablespoon", "IM tbs", lambda x: x*0.0177582, lambda x: x/0.0177582),
    Unit("Imperial teaspoon", "IM ts", lambda x: x*(0.00591939), lambda x: x/(0.00591939))],
  "temperature":[
    Unit("degree celcius", "C", Unit.useless_func, Unit.useless_func),
    Unit("fahrenheit", "F", lambda x: (x-32)*(5/9), lambda x: (x*9/5)+32),
    Unit("kelvin", "K", lambda x: x - 274.15, lambda x: x - 274.15)]}
type_of_units = list(UNIT_DATA.keys());


def find_in_UNIT_DATA(unit_type, target):
  """
    Find Unit object in UNIT_DATA data structure
  """
  for i in UNIT_DATA[unit_type]:
    if i.unit_name == target: return i

def get_unit_names_in_UNIT_DATA(unit_type):
  """returns a list of name in unit type

  Args:
      unit_type (string): is a key in the UNIT_DATA dictionary
  """
  return [x.unit_name for x in UNIT_DATA[unit_type]]

def index(request):
  return render(request, 'home/nav_layout.html',{
    "classification":"Type of units", 
    "name_app": "conversion",
    "nav_name": zip(type_of_units, map(lambda x: x.capitalize(), type_of_units)),
    "title": "Unit Types",
    "heading": "Unit Types"
  })

def handle_type(request, unit_type):
  dict_to_send = {
    "title": unit_type.capitalize(),
    "heading": f"{unit_type.capitalize()} unit converter",
    "classification": f"{unit_type.capitalize()} unit converter",
    #"units":[("feet", "ft"), ("inch", "in"), ("meter", "m")],
    # "units_output": zip([x.unit_name for x in UNIT_DATA[unit_type]], [x.unit_abbr for x in UNIT_DATA[unit_type]]),
    "units": [x.get_name_and_abbr() for x in UNIT_DATA[unit_type]],
    "result":None
  }
  if request.method == "POST":
    #return HttpResponse(request.read())
    dict_to_send["result"] = find_in_UNIT_DATA(unit_type, request.POST["input-unit"]).cvt(float(request.POST['input-box']), find_in_UNIT_DATA(unit_type, request.POST["output-unit"]))
  return render(request, 'conversion/index.html', dict_to_send)
  