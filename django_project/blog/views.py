from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostViewList(ListView):
    model = Post
    # Template looskup pattern -> <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
