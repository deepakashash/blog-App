from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse

# import models 
from .models import *


@login_required
def index(request):
    if request.method == 'GET':
        blog_items = BlogItem.objects.filter(user=request.user)
      
        context = {
            'blogs': blog_items
        }
        # use render import  - give the request
        return render(request, 'blogapp/index.html', context)
    
    if request.method == 'POST':
        blog_item = BlogItem()
        blog_item.title = request.POST['title']
        blog_item.post = request.POST['post']
        blog_item.user = request.user
        blog_item.save()
        return HttpResponseRedirect(reverse ('blogapp:index'))
    
    return HttpResponseBadRequest()

@login_required
# convention to call ID for primary key
def details(request, pk):
    blog = get_object_or_404(BlogItem, pk=pk, user=request.user)
    
    if request.method == 'GET':
        context = {
            'blog': blog
        }
        return render(request,'blogapp/details.html', context)

    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.post = request.POST.get('post')
        blog.save()
        return HttpResponseRedirect(reverse ('blogapp:index'))

    return HttpResponseBadRequest()


