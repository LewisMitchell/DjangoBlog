from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post
# Create your views here.

def index(request):
    latest_posts = Post.objects.order_by("-created_at")[:5]
    page = loader.get_template('blog/index.html')
    context = {
        'posts': latest_posts
    }
    return HttpResponse(page.render(context, request))