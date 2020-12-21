from django.shortcuts import render
from unitconverterapp.models import *

def home(request):
    
    measurements = Measurement.objects.all()
    units = Unit.objects.all()
    conversions = Conversion.objects.all()
   
   
    return render(request, 'home.html', {'measurements':measurements, 'conversions':conversions, 'units':units})


def measurement_view(request):
    measurement_id = request.GET.get('measurement')
    measurement = None
    
    if measurement_id is not None:
        try:
            measurement = Measurement.objects.get(pk=measurement_id)
        except Measurement.DoesNotExist:
            pass

    measurement = MeasurementArticle.objects.filter(measurement=measurement).get(measurement_id=measurement_id)
    measurements = Measurement.objects.all()
   
    
    return render(request, 'measurements_article.html', {'measurement':measurement, 'measurements':measurements, })   


def unit_view(request):
    unit_id = request.GET.get('unit')
    unit = None
    if unit_id is not None:
        try:
            unit = Unit.objects.get(pk=unit_id)
        except Unit.DoesNotExist:
            pass
    unit = UnitArticle.objects.filter(unit=unit).get(unit_id=unit_id)
    units = Unit.objects.all()
    return render(request, 'unit_article.html', {'unit':unit, 'units':units })
    
def unitconvert(request, converter_name=None):
    measurement_type_id = request.GET.get('measurement_type')
    
    converter = None
    measurement_type = None
    

    if converter_name is not None:
        try:
            converter = Conversion.objects.select_related('from_unit', 'from_unit__measurement_type', 'to_unit').get(name=converter_name)
        except Conversion.DoesNotExist:
            pass
    if measurement_type_id is not None:
        try:
            measurement_type = Measurement.objects.get(pk=measurement_type_id)
        except Measurement.DoesNotExist:
            pass


    if converter is None:
        converter = Conversion.objects.select_related('from_unit', 'from_unit__measurement_type', 'to_unit')
        if measurement_type is not None:
            converter = converter.filter(from_unit__measurement_type=measurement_type)
        converter = converter.first()
    
    measurements = Measurement.objects.all()
    
    if converter is not None:
        converter.inverse_rate = (1.0 / converter.rate);
        converters = Conversion.objects.filter(
            from_unit__measurement_type=converter.from_unit.measurement_type
        ).exclude(pk=converter.pk)
    else:
        converters = None

      
    
    return  render(request, 'unit_convert_page.html', { 
        'converters': converters,
        'conversion': converter,
        'measurements': measurements,
    })


    
          

    
