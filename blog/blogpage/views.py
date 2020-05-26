from django.shortcuts import render,HttpResponse
from blogpage.models import Post

# Create your views here.


def bloghome(request):
    allposts = Post.objects.all()
    
    context={'allposts': allposts}
    return render(request,'blogpage/bloghome.html',context)

def blogpost(request, slug):
    post= Post.objects.filter(slug=slug)[0]
    context={'post': post}
    return render(request,'blogpage/blogpost.html', context)

