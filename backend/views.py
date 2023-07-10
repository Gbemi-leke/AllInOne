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

from django.contrib import messages
from frontend.models import *
from backend.forms import *
# Password Reset
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
 #  end

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

def password_reset_request(request):
    if request.method == "POST":
        domain = request.headers['Host']
        password_reset_form = PasswordReset(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            # You can use more than one way like this for resetting the password.
            # ...filter(Q(email=data) | Q(username=data))
            # but with this you may need to change the password_reset form as well.
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "backend/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000/',
                        'site_name':'ALLINONE',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'josepholuwagbemi02@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordReset()
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form = subscribe_form.save(commit=False)
            subscribe_form.user = request.user
            subscribe_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('frontend:password_reset_request')
    else:
        subscribe_form = SubscribeForm()
    return render(request=request, template_name="backend/password_reset.html",
                  context={"password_reset_form": password_reset_form,'subscribe_form':subscribe_form})

@login_required(login_url='/backend/login/')
def add_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog_form = blog_form.save(commit=False)
            blog_form.user = request.user
            blog_form.save()
            messages.success(request, 'Add successfully.')
            return redirect('backend:add_blog')
    else:
        blog_form = BlogForm()
    return render(request, 'backend/add_blog.html', {'blog_form': blog_form})

@login_required(login_url='/backend/login/')
def edit_blog(request, post_id):
    blog_post = get_object_or_404(Blog, id=post_id)
    if request.method == 'POST':
        editblog_form = EditBlogForm(request.POST, request.FILES,instance=blog_post)
        if editblog_form.is_valid():
            editblog_form = editblog_form.save(commit=False)
            editblog_form.user = request.user
            editblog_form.save()
            messages.success(request, 'Successfully Edited.')
            editblog_form = EditBlogForm(instance=blog_post)
            
    else:
        editblog_form = EditBlogForm(instance=blog_post)
    return render(request, 'backend/edit_blog.html', {'editblog_form': editblog_form})

@login_required(login_url='/backend/login/')
def view_blog(request, view_id):
    post = Blog.objects.filter( id=view_id)
    return render(request, 'backend/view_blog.html', {'pst':post})


@login_required(login_url='/backend/login/')
def list_all_blog(request):
    list_all_blog = Blog.objects.order_by('-blog_date')[:20]
    return render(request, 'backend/list_all_blog.html', {'list_blog':list_all_blog})


@login_required(login_url='/backend/login/')
def delete_blog(request, delete_id):
    blog_record = get_object_or_404(Blog, id=delete_id)
    blog_record.delete()
    return redirect('backend:list_all_blog')

@login_required(login_url='/backend/login/')
def preview(request, agent):
    file = get_object_or_404(Blog, pk=agent)
    return render(request, 'backend/preview.html', {'post':file})
