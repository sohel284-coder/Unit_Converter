from django.urls import path, include
from unitconverterapp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('measurement', views.measurement_view, name='measurement_view'),
    path('unit', views.unit_view, name='unit_view'),
    path('convert', views.unitconvert, name='unitconvert'),
    path('<slug:converter_name>', views.unitconvert, name='converter'),
  
]

