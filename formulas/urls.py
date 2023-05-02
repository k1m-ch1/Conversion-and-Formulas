from django.urls import path
from . import views

app_name = "formulas"

urlpatterns = [
    path('', views.index, name="nav")
]

