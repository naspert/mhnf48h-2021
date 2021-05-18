from django.urls import path
from . import views


app_name = "field"
urlpatterns = [
    path('', views.home, name='home')
]