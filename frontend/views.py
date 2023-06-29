from django.shortcuts import render
from django.http import HttpResponse

# from Olamide.frontend.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from frontend.models import *
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
    return render(request, 'frontend/index.html', {'blog':blogs})

def about(request):
    return render(request, 'frontend/about.html')

def foods(request):
    return render(request, 'frontend/foods.html')

def phones(request):
    return render(request, 'frontend/phones.html')

def wears(request):
    return render(request, 'frontend/wears.html')

def cakes(request):
    return render(request, 'frontend/cakes.html')

def contact(request):
    return render(request, 'frontend/contact.html')

def blog(request):
    blogs = Blog.objects.order_by('-blog_date')[:6]
    return render(request, 'frontend/blog.html', {'blog':blogs})

def hostel(request):
    return render(request, 'frontend/hostel.html')
