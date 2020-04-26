from django.urls import path
from . import views

urlpatterns = [
    path('', views.corona, name="coronatracker"),
    path('country/', views.country, name="country")
]