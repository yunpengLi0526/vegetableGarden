from django.shortcuts import render
from django.http import HttpRequest
from raidCheck import models

# Create your views here.

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")

def index(request):
    blog_index = models.Article.objects.all().order_by('-id')
    context = {
        'blog_index':blog_index,
    }
    return render(request,'index.html',context)