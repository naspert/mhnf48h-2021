from django.contrib import admin
from field.models import Observation


class ObservationAdmin(admin.ModelAdmin):
    model = Observation

admin.site.register(Observation, ObservationAdmin)
