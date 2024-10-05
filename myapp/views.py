
from email.mime import image
from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout 

def index(request):
    return render(request,'home/index.html')

#def blogPost(request , slug):
 #  return HttpResponse(f'this is blogPost : {slug}')

def cont(request):
    return render(request,'home/contact.html')

def bloghome(request):
    allPosts= Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request,'blog/bloghome.html',context)

def about(request):
     A = request.GET['name']
     alter = Post.objects.filter(uname = A)
     context = {'user':request.user , 'alter':alter} 
     return render(request , 'home/about.html' , context)

def contact_save(request):
        if request.method=='POST':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            content = request.POST['content']
            #return HttpResponse( name, email , phone,content)
            if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4 :
                messages.error(request,'welcome to contact')
                return HttpResponse('done')
            else:
                C= contact(name=name , email =email, phone=phone, content=content )
                C.save()
                messages.success(request,'success')                   
                return HttpResponse('done')
        else:
            return HttpResponse('FAILED')

def blogPost(request , slug):
   post = Post.objects.filter(slug=slug).first()
   comments= blogcomment.objects.filter(post=post)
   context = {'post':post , 'comments':comments , 'user':request.user}
   return render(request, 'blog/blogPost.html',context)

def search(request):
    query=request.GET['query']
    if len(query)>70:
        allPosts = Post.objects.none()
    else :
        allPoststitle= Post.objects.filter(title__icontains=query)
        allPostscontent= Post.objects.filter(content__icontains=query)
        allPosts = allPoststitle.union(allPostscontent)
    sr = {'allPosts':allPosts , 'query':query}
    return render(request, 'home/search.html',sr)

def Sign_up(request): 
        if request.method =='POST':
            Username=request.POST['Username']
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            pass1=request.POST['pass1']
            pass2=request.POST['pass2']
            #Check for enomerous input
            if len(Username) > 15:
                 messages.error(request,'Username must be under 15 character')
                 return redirect('/')
            if not Username.isalnum():
                 messages.error(request,'please enter only alpha-numeric username')
                 return redirect('/')
            if pass1 != pass2:
                 messages.error(request,'passwords do not mach')
                 return redirect('/')
            myuser = User.objects.create_user(Username,email,pass1,image)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request,'done')
            return redirect('/')

        else:
            return HttpResponse('failed')

def log_out(request): 
        logout(request) 
        messages.success(request,"Successfully logged out")
        return redirect('/')
      
def log_in(request):
      if request.method =='POST':
            loginusername=request.POST['loginusername'] 
            loginpassword=request.POST['pass'] 
            user = authenticate(username = loginusername , password= loginpassword)
            if user is not None :
                login(request , user)
                messages.success(request," successfully logged in ")
                return redirect('/')
            else:
                messages.error(request,"Invalid Credentials , Please try again")
                return redirect('/')
      else:
            return HttpResponse('failed')

def postcomment(request):
    if request.method == 'POST':
       
               comment=request.POST['comment']
               user = request.user
               postSno = request.POST["postSno"]
               post = Post.objects.get(sno=postSno)
               Comment = blogcomment(comment=comment , user=user , post =post)
               Comment.save()
               messages.success(request,"your comment has been posted successfully")
               return redirect(f"/{post.slug}")
               
    else:
        return HttpResponse('failed')

def post(request):
    return render(request,'blog/addpost.html')

def addpost(request):
    if request.method =='POST':
        heading = request.POST['heading']
        slug = request.POST['heading']
        matter = request.POST['matter']
        author = request.user
        post = Post( uname = author ,title = heading , slug = slug , author = author , content =matter)
        post.save()
        messages.success(request,"Your post has been successfully added")
        return redirect('/')
    else:
        return HttpResponse("failed") 

def profile(request):
    A = request.user.username
    alter = Post.objects.filter(uname = A)
    context = {'user':request.user , 'alter':alter} 
    return render(request , 'blog/profile.html' , context)

def delete(request):
      roll=request.GET['sr']
      s=Post.objects.filter(sno=roll)
      s.delete()
      return redirect('/profile')

def update(request):
      if request.method=='POST':
          s=Post.objects.get(sno=request.POST['up'])
          s.title=request.POST['heading']
          s.content=request.POST['matter']
          s.save()
          return redirect('/profile')


      else:
           roll=request.GET['up']
           s=Post.objects.get(sno=roll)
           send = {'update':s , 'roll':roll}
           return render(request,'blog/update.html', send)
