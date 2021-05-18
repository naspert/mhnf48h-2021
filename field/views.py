from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Sample

@login_required
def home(request):
    render(request, 'home.html')

