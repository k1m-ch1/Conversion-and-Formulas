from django.urls import path, include
from . import views

app_name = "conversion"

urlpatterns = [
    path('', views.index, name="nav"),
    path('<str:type>/', views.handle_type, name="length"),
]
