from django.shortcuts import render
from datetime import date
from django.contrib.auth.decorators import login_required
import requests
from settings.models import Settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from system.models import *
from system.forms import AddEquipmentForm, UpdateStatusForm
from django.contrib import messages




# Create your views here.
@login_required
def dashboard(request):
    dt = date.today()   

    gen_settings = Settings.objects.get(id=1)
    context = {
        'main_machine': gen_settings.main_machine,
        'title': 'Dashboard',
        'head': 'Machines',
        
        'date': dt,        

    }

    if gen_settings:
        request.session['main_machine'] = gen_settings.main_machine
    else:
        request.session['main_machine'] = ""
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def equipment_view(request):
    machines = Equipment.objects.all()

    print(machines)
    gen_settings = Settings.objects.filter(id=1).first()
    if gen_settings:
        request.session['main_machine'] = gen_settings.main_machine
    else:
        request.session['main_machine'] = ""

    context = {
        'title': 'Equipment Display',
        'head': 'Equipment',
        'machines': machines
    }
    return render(request, "dashboard/equipment.html", context)

@login_required
def add_equipment(request):
    if request.method == 'POST':
        form = AddEquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save()

    else:
        form = AddEquipmentForm()
    gen_settings = Settings.objects.get(id=1)
    context = {
        'main_machine': gen_settings.main_machine,
        'title': 'Add Equipment',
        'head': 'Add Equipment',
        'form': form
    }
    return render(request, 'dashboard/addEquipment.html', context)

@login_required
def updatestatus(request, pk):

    machine = get_object_or_404(Equipment, id=pk)
    print(machine)
    try:
        sts = Equipment.objects.get(pk=pk)

        if sts:
            STATUS = sts.status
    except:

        print("The user doesn't exist")
    if request.method =='POST':
        form = UpdateStatusForm(request.POST or None, instance=machine)
        if STATUS == 1:
            action = 0
        else:
            action = 1
        if form.is_valid():
            form.save()
            messages.success(request, f'Machine Status updated Successfully.')
            return redirect('show-equipment')
    else:
        form = UpdateStatusForm(instance=machine)

    gen_settings = Settings.objects.get(id=1)
    context = {
        'main_machine': gen_settings.main_machine,
        'title':'Update Status',
        'head': 'Update Equipment Status',
        'page_nick': 'e-update',
        'form': form,
        'equipment_id':pk

    }
    
    return render(request, 'dashboard/updateEquipment.html', context)