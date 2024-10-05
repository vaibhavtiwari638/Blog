from django.urls import path
from blog.views import *

urlpatterns = [
 #   path('bloghome',bloghome,name='blog'),
     path('<str:slug>',blogPost,name='blogPost'),
]