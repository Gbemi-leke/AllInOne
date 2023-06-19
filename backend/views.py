from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from django.views.generic import ListView
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User 

from django.contrib import messages
from frontend.models import *
# from backend.forms import *
# Password Reset
from django.conf import settings
# Create your views here.


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
    return render(request, 'frontend/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')