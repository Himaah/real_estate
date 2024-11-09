

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Real_estate_property
from .forms import PropertyForm

def list_properties(request):
    properties = Real_estate_property.objects.all()
    location = request.GET.get('location')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    return render(request, 'listings/property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Real_estate_property, pk=pk)
    return render(request, 'listings/property_detail.html', {'property': property})

def create_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_properties')
    else:
        form = PropertyForm()
    return render(request, 'listings/property_form.html', {'form': form})

def delete_property(request, pk):
    property = get_object_or_404(Real_estate_property, pk=pk)
    if request.method == "POST":
        property.delete()
        return redirect('list_properties')
    return render(request, 'listings/property_confirm_delete.html', {'property': property})