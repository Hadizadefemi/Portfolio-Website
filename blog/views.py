from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def blog_index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, "blog_index.html", context)

def blog_detail(request, pk):
    pass