from django.urls import path
from . import views
import field.forms as forms

app_name = "field"
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', forms.ObservationCreate.as_view(), name='observ_create'),
    path('update/<int:pk>/', forms.ObservationUpdate.as_view(), name='observ_update'),
    path('delete/<int:pk>/', forms.ObservationDelete.as_view(), name='observ_delete'),
    path('all/', views.show_all, name='show_all'),
    path('csv-all/', views.ObservationExportView.as_view(), name='csv_export_all')
]