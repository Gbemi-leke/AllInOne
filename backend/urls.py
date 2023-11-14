from django.urls import path
from django.conf.urls import url 
from backend import views

app_name = 'backend'

urlpatterns = [  
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout_view-page/', views.logout_view, name='logout_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload-blog/', views.add_blog, name='add_blog'),
    path('delete-blog/<int:delete_id>', views.delete_blog, name='delete_blog'),
    path('list_all_blog/<int:post_id>', views.edit_blog, name='edit_blog'),
    path('view_preview/<int:agent>', views.preview, name='preview'),
    path('subscribers/', views.newsletter, name='newsletter'),
    path('messages/', views.message, name='message'),
    path('change-password/', views.change_password, name='change_password'),
    path('view_blog/<int:view_id>', views.view_blog, name='view_blog'),
    path('list_all_blog/', views.list_all_blog, name='list_all_blog'),
     path('change_password/', views.change_password, name='change_password'),
    path('password_reset/', views.password_reset_request, name='password_reset_request'),

]