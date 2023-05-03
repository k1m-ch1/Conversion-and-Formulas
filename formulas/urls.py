from django.urls import path
from . import views

app_name = "formulas"

urlpatterns = [
    path('', views.index, name="nav"),
    path('<str:type>/', views.handle_type),
    path('<str:formula_type>/<str:formula>/', views.handle_formula)
]

