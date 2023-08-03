from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Models
from django.contrib import messages
from users.models import *
from users.forms import *

# Create your views here.


@login_required(login_url='/backend/login/')
def user_profile(request):
    return render(request, 'backend/user_profile.html')

@login_required(login_url='/backend/login/')
def edit_profile(request):
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'User edited successfully.')
            # return edit_form.save()

        else:
            messages.success(request, 'User edited unsuccessfully.')
            
    else:
        edit_form = EditUserForm(instance=request.user)
    return render(request, 'backend/edit_profile.html', {'edit_key':edit_form})