# admin_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Plants
from .forms import PlantForm # Assuming you have a PlantForm in forms.py

def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller_app:add_plant') # Redirect back to the page after adding a plant
    else:
        form = PlantForm()

    plants = Plants.objects.all()
    return render(request, 'seller_app/add_plant.html', {'form': form, 'plants': plants})

def delete_plant(request, pk):
    plant = get_object_or_404(Plants, pk=pk)
    plant.delete()
    return redirect('seller_app:add_plant') # Redirect back to the add plant page after deleting a plant

