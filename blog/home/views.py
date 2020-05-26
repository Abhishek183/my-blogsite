from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from blogpage.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.db import IntegrityError

# Create your views here.

def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        if len(name)<1 or len(email)<2 or len(password)<1:
            messages.error(request,'fill the form correctly')
            return redirect('contact')
        else:
            contact=Contact(name=name, email=email , password=password)
            contact.save()
            messages.success(request, 'submitted')
    return render(request,'home/contact.html')


def handlesignup(request):
    if request.method=='POST':
        name1=request.POST['name1']
        email=request.POST['email']
        pass1=request.POST['pass1']
        if len(name1)>10 or len(pass1)<2:
            messages.error(request,"password is short or name is short")
            return redirect('/')
        myuser = User.objects.create_user(name1,email,pass1)
        myuser.save()
        messages.success(request,"submitted sucesfully")
        return redirect('/')
    else:
        return HttpResponse('404 -Not found') 


def handlelogin(request):
    if request.method == 'POST':
        # Get the post parameters
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(username=name, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"succesfully logedin")
            return redirect('home')
            
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('login')
            
    return HttpResponse('404 - Not Found')



def handlelogout(request):
    logout(request)
    messages.success(request,"succesfully logout")
    return redirect('home')

   


def addpost(request):
    return render(request,'home/addpost.html')

def submit(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content= request.POST.get('content')
        author=request.POST.get('author')
        if len(title)>1 and len(content)>1 and len(author)>1:
            new_blog = Post(title=title,content=content,author=author)
            new_blog.save()
            messages.success(request,"submitted sucesfully")
            return redirect('bloghome')
        else:
            messages.error(request,"expand the things")
            return redirect('addpost')
    return redirect('home')