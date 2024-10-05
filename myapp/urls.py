from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',index,name='index'),
    path('home',index,name='index'),
    path('contact',cont,name='contact'),
    path('blog_home',bloghome,name='name'),
    path('about',about,name='contact'),
    path('contact_save',contact_save,name='contact'),
    path('search',search,name='search'),
    path('signup',Sign_up,name='signup'),
    path('log_out',log_out,name='log_out'),
    path('log_in',log_in,name='log_in'),
    path('post',post,name='post'),
    path('addpost',addpost,name='addpost'),
  
    
    path('postcomment',postcomment,name='postcomment'),
    path('profile' , profile , name='profile'),
    path('delete',delete , name = 'delete'),
    path('update' ,update , name='showupdate'),
    path('<str:slug>',blogPost,name='blogPost'),
    
    
   
 #   path('<str:slug>',blogPost,name='blogPost'),
    
]