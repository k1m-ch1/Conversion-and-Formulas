# Conversion-and-Formulas
Simple Django project for converting units and calculating formulas of different things.

# Platforms
- is built using Django.

# How to runserver on local machine
## Assumption
- you have python installed

## Installing Django
1. Open up terminal
2. type "pip install django" (no virus I swear)
```
pip install django
```

## Runserver
1. go to the directory with manage.py (in the first file)
2. run this command in the terminal: "python manage.py runserver"
```
python manage.py runserver
```
3.Enter that local https address (should be https://127.0.0.1:8000 but should be printed after you enter the command in step 2)

# Apps
- there are three apps, home, conversion and formulas.

## home

### Overview
- the home app has most of the templates for the rest of the app.
- it has layout.html which is used as a template for some of the pages and nav_layout.html which is used as a template for the navigation pages.

### urls.py
- just calls the some function in views.py where it just display index.html which is the default home page

## conversion

### Overview
- is the conversion part of the web app

### urls.py
- has path linked to the home navigation path('', ...)
- has path linked to the the conversion interface path('<str:unit_type>")

### views.py
- has class *Unit* which has a few information on the unit and a few methods to perform on those units
- has that goofy ahh made up data structure called *UNIT_DATA*

### *UNIT_DATA*
- UNIT_DATA is a dictionary catagorized by the unit type (length, area, temperature, ...)
- the values in the dictionary will contain a bunch of *Unit* class representing the units.
- the first few of the parameters are self-explanatory but the higher order functions needs further explaination
- the first of the higher order fuction will convert to a base unit (length is meter, area is square meter, ...)
- the second of the higher order function will convert from the base unit back to the unit.


## formulas
### Overview
- is the formula part of the web app

### urls.py
- has path linked to the nav: path('', ...)
- has path linked to the nav of type: path('<str:type>')
- has path linked to the formula interface path('<str:formula_type>, <str:formula>, ...)

### views.py
- has *formula* class (didn't follow naming convention cuz didn't start with capital)
- has *formula* class needs a goofy ah made up data structure (4d array)

#### 4d array
- Overview: this array is just a way to represent some generic math formulas. (it can do +, -, *, / operation but doesn't have sqrt(), raise to power, raise to log and stuff like that. (can apply but only to the whole thing for example can still do 
```python
sqrt(pow(a, 2) + pow(b, 2)))
```
but not 
```python
sqrt(pow(a, 2)) + sqrt(pow(b, 2))
```
- first array is a list which will gets added together through functools.reduce(add, *insert 4d array*(not real syntax),  0)
- second array is a tuple of size constant size 2 which represents a fraction with nominator and denominator
- third array is a tuple representing stuff that will get multiplied together through functools.reduce(mul, *insert 2d tuple*(not real syntax), 1)
- fourth array is a tuple representing the unit name and unit abbreviation Ex. ('meter', 'm')


# stuff to improve
1. better styling (css file in home/static/home/styles.css)
2. clean up the code (rip UNIT_DATA)
3. better docstrings for each function
4. since UNIT_DATA didn't follow DRY(Don't Repeat Yourself) principle and I manually typed in all of the lambda functions, there **will** be bugs but I'm too lazy to check for everthing so plz check for me if can.
5. for formulas, the result doesn't have a unit because I didn't implement sth that stores the unit and pass it into the html file so that can be improved on. For now, there's just a google search button for more information about units, formula and a general google search.



