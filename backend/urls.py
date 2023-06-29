from django.urls import path
from django.conf.urls import url 
from backend import views

app_name = 'backend'

urlpatterns = [  
    path('login/', views.login_view, name='login_view'),
    path('logout_view-page/', views.logout_view, name='logout_view'),
    path('dashboard/', views.dashboard, name='dashboard'),

]