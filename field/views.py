import csv
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.db.models import Count
from csv_export.views import CSVExportView
from .models import Observation


@login_required
def home(request):
    user_obs = Observation.objects.filter(owner=request.user)
    return render(request, 'field/home.html', {'observations': user_obs})


@login_required
def show_all(request):
    obs = Observation.objects.all()
    return render(request, 'field/all.html', {'observations': obs})


@method_decorator(login_required, name='get')
class ObservationExportView(CSVExportView):
    model = Observation
    fields = ('owner__username', 'species', 'search_term', 'preferred_name', 'remarks', 'created_date', 'last_modified_date')


@login_required
def show_stats(request):
    obs_per_user = User.objects.annotate(num_obs=Count('observation')).filter(num_obs__gt=1).order_by('num_obs')
    return render(request, 'field/stats.html', {'observations': obs_per_user})






