from django.shortcuts import render

from django.http import HttpResponse

def bloghome(request):
    return render(request ,'blog/bloghome.html')

def blogPost(request):
    return render(request, 'blog/blogPost.html')

# Create your views here.
def blogPost(request , slug):
   return render(request, 'blog/blogPost.html')