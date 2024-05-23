
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('city/<city>', views.analysis_city)
]
