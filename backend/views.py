# from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
# from django.contrib.auth.models import User

from django.contrib import messages
from frontend.models import *
from backend.forms import *


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  

        if user is not None:
            login(request, user)
            return render(request, 'backend/index.html')
        else:
            messages.error(request, 'Username and Password do not match')    
    return render(request, 'frontend/signup.html')

@login_required(login_url='/backend/login/')
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='/backend/login/')
def dashboard(request):
    list_all_blog = Blog.objects.order_by('-blog_date')[:4]
    return render(request, 'backend/index.html', {'list_blog':list_all_blog})

@login_required(login_url='/backend/login/')
def message(request):
    contact = Contact.objects.all()
    return render(request, 'backend/contact.html', {'contact':contact})

@login_required(login_url='/backend/login/')
def newsletter(request):
    newsletter = SubscribeModel.objects.order_by('-timestamp')
    return render(request, 'backend/newsletter.html', {'newsletter':newsletter})

@login_required(login_url='/backend/login/')
def change_password(request):
    if request.method == 'POST':
        change_password = PasswordChangeForm(data=request.POST,
        user=request.user)
        if change_password.is_valid():
            change_password.save()
            update_session_auth_hash(request, change_password.user)
            messages.success(request, 'Password changed successfully.')
    else:
        change_password = PasswordChangeForm(user=request.user)
    return render(request, 'backend/change_password.html', {'pass_key':change_password})

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
    else:
        edit_form = EditUserForm(instance=request.user)
    return render(request, 'backend/edit_profile.html', {'edit_key':edit_form})