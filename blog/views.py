from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from .models import Post, Comment, PostImage
from .forms import CommentForm

# Create your views here.


def homepage(request):

    posts = Post.objects.all()

    return render(request, 'homepage.html', {
        'posts': posts,
    })


def post(request, pk):

    post = get_object_or_404(Post, pk=pk)
    images = PostImage.objects.filter(post=post)
    comments = Comment.objects.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.content = form['content'].value()
            comment.author_name = form['author_name'].value()
            comment.author_surname = form['author_surname'].value()
            comment.author_email = form['author_email'].value()
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('/')
    else:
        form = CommentForm()

    return render(request, 'post.html', {
        'post': post,
        'images': images,
        'comments': comments,
        'form': form,
    })


def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        result = Post.objects.all().filter(title__contains=search)

    return render(request, 'search_result.html', {
        'posts': result
    })
