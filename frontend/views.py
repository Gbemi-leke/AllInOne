from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import ListView

# from Olamide.frontend.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from frontend.models import *
from backend.forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# for sending mail import
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils.html import strip_tags
# end

# Create your views here.

def index(request):
    blogs = Blog.objects.order_by('-blog_date')[:6]
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('index')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/index.html', {'blog':blogs, 'subscribe_form':subscribe_form})


def about(request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:about')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/about.html', {'subscribe_form':subscribe_form})

def foods(request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:foods')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/foods.html', {'subscribe_form':subscribe_form})

def phones(request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:phones')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/phones.html', {'subscribe_form':subscribe_form})

def wears(request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:wears')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/wears.html', {'subscribe_form':subscribe_form})

def cakes(request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:cakes')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/cakes.html', {'subscribe_form':subscribe_form})

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if  contact_form.is_valid():
            contact_form = contact_form.save(commit=False)
            contact_form.user = request.user
            contact_form.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('frontend:contact')
    else:
        contact_form =ContactForm()
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:contact')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/contact.html', {'cont':contact_form,'subscribe_form':subscribe_form})

def blog(request):
    blogs = Blog.objects.order_by('-blog_date')[:6]
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:blog')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/blog.html', {'blog':blogs, 'subscribe_form':subscribe_form})

def blog_details(request, detail_id):
    detail =Blog.objects.get(id=detail_id)
    return render(request, 'frontend/blog_details.html', {'det':detail})

def hostel(request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:hostel')
    else:
        subscribe_form = SubscribeForm()
    return render(request, 'frontend/hostel.html', {'subscribe_form':subscribe_form})
