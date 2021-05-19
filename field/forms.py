from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from field.models import Observation
from django.utils.timezone import localtime


@method_decorator(login_required, name='dispatch')
class ObservationCreate(CreateView):
    model = Observation
    fields = ['species', 'remarks']
    initial = {'created_date': localtime(), 'last_modified_date': localtime() }

    def form_valid(self, form):
        owner = self.request.user
        form.instance.owner = owner
        return super(ObservationCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('field:home')


@method_decorator(login_required, name='dispatch')
class ObservationUpdate(UpdateView):
    model = Observation
    fields = ['species', 'remarks']

    def form_valid(self, form):
        form.instance.last_modified_date = localtime()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        obj = super(ObservationUpdate, self).get_object(queryset=queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied()
        return obj

    def get_success_url(self):
        return reverse_lazy('field:home')


@method_decorator(login_required, name='dispatch')
class ObservationDelete(DeleteView):
    model = Observation
    success_url = reverse_lazy('field:home')