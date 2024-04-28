from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import EditForm, PostForm
from .models import Category, Post

# def home(request):
#     return render(request, 'home.html', {})


class HomeViev(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-post_date"]
    # ordering = ['-id']

def CategoryView(request, cats):
    return render(request, 'categories.html', {'cats': cats})


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = '__all__'
    # fields = ('body', 'title')


class AddCategoryView(CreateView):
    model = Category
    template_name = "add_category.html"
    fields = "__all__"


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")
