from django.shortcuts import render,  HttpResponse, get_object_or_404, redirect
from .forms import AddUserForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Settings



def get_users(request):
    users = User.objects.all()

    context = {
        'title': 'Users',

        'head': 'User Settings',
        'users': users,
    }

    return render(request, 'settings/users_list.html', context)



@login_required
def general_info(request):
    
   

    
    context = {
        "page_nick": 'general-info',
        'title': 'Settings',
        "head": "Settings",
        
        
    }
    return render(request, "settings/settings_home.html", context)

# Create your views here.
@login_required  # create crop
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            message = f'New user "{user.username}" was successfully created.'
            messages.success(request, message)

            return redirect('users')
    else:
        form = AddUserForm()

    gen_settings = Settings.objects.get(id=1)

    context = {
        'main_machine': gen_settings.main_machine,
        'title': 'Add User',
        'head': 'Add User',
        'form': form
    }
    return render(request, 'settings/add_user.html', context)