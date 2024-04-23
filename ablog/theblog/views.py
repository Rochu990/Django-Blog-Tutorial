from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from .models import Post
from .forms import PostForm, EditForm

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
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('body', 'title')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']




