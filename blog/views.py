from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog
from datetime import datetime
# Create your views here.
def home(request):
	post_list = Blog.objects.all()
	return render(request,'home.html',{'post_list':post_list})

