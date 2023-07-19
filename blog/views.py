from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
def blog_index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, "blog/blog_index.html", context)

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                post = post
            )
            comment.save()
            return HttpResponseRedirect(reverse('blog_detail', args=str((post.pk))))
    
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/blog_detail.html", context)