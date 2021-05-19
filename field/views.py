from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Observation


@login_required
def home(request):
    user_obs = Observation.objects.filter(owner=request.user)
    return render(request, 'field/home.html', {'observations': user_obs})



