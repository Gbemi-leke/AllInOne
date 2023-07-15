from django.urls import path
from django.conf.urls import url 
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('foods/', views.foods, name='foods'),
    path('wears/', views.wears, name='wears'),
    path('phones/', views.phones, name='phones'),
    path('cakes/', views.cakes, name='cakes'),
    path('blog/', views.blog, name='blog'),
    path('hostel/', views.hostel, name='hostel'),
    path('contact/', views.contact, name='contact'),
    path('detail/<int:detail_id>/', views.blog_details, name='blog_details'), 

]