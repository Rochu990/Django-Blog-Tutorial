from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView

from .models import Post

# def home(request):
#     return render(request, 'home.html', {})


class HomeViev(ListView):
    model = Post
    template_name = "home.html"


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'
    # fields = ('body', 'title')

