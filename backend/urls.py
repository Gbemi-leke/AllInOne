from django.urls import path
from django.conf.urls import url 
from backend import views

app_name = 'backend'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout_view-page/', views.logout_view, name='logout_view'),
    # path('', views.about, name='about'),
    # path('portfolio/', views.portfolio, name='portfolio'),
    # path('blog/', views.blog, name='blog'),
    # path('details/<int:blog_id>/', views.detail_blog, name='detail_blog'), 
    # path('contact/', views.contact, name='contact'),

]