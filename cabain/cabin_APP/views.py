from django.shortcuts import render, redirect
from cabin_APP.forms import FormRegion, FormCity
from cabin_APP.models import Region, City

# Create your views here.

def listado_regiones(request):
    regiones = Region.objects.all()
    context = {'regiones': regiones}
    return render(request, 'regiones.html', context)

def ingresar_region(request):
    form = FormRegion()
    if request.method == 'POST':
        form = FormRegion(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listado_regiones)
    context = {'form': form}
    return render(request, 'ingresar_region.html', context)

def listado_ciudades(request):
    ciudades = City.objects.all()
    context = {'ciudades': ciudades}
    return render(request, 'ciudades.html', context)

def ingresar_ciudades(request):
    form = FormCity()
    if request.method == 'POST':
        form = FormCity(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listado_ciudades)
    context = {'form': form}
    return render(request, 'ingresar_ciudad.html', context)