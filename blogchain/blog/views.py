# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from blog.models import Blog,Contact
import math

# Create your views here. boingop utility 
blogs="heloblog"
def home(request):
    return render(request,'index.html')

def blog (request):
    global blogs
    no_of_post=4
    #if request.GET['pageno']
    page=request.GET.get('page')
    if page is None:
        page=1
    else:
        page=int(page)
    print(page)
    blogs=Blog.objects.all()
    length=len(blogs)
    print(length)
    blogs=blogs[(page-1)*no_of_post:page*no_of_post]
    if page>1:
        prev=page-1
    else:
        prev=None
    if page<math.ceil(length/no_of_post):   
        nxt=page+1
    else:
        nxt=None
    
    context={'blogs':blogs,'prev':prev,'nxt':nxt}
    
    return render(request,'bloghome.html',context)

def blogpost(request,slug):
    blog=Blog.objects.filter(slug=slug).first()
    context={'blogs':blogs}
    return render(request,'blgpost.html',context)

def contact(request ):
    if request.method == 'POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        dtext=request.POST.get("dtext")
        #now we have to store all this in databse 
        instance=Contact(name=name,email=email,phone=phone,dtext=dtext)
        instance.save()
    return render(request,'contact.html')

def search(request):
    return render(request,'search.html')