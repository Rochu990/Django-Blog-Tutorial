from django.urls import path

# from . import views
from .views import (
    AddCategoryView,
    AddPostView,
    ArticleDetailView,
    CategoryListView,
    CategoryView,
    DeletePostView,
    HomeViev,
    UpdatePostView,
)

urlpatterns = [
    # path("", views.home, name="home")
    path("", HomeViev.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name="update-post"),
    path("article/<int:pk>/remove", DeletePostView.as_view(), name="delete-post"),
    path("add_category/", AddCategoryView.as_view(), name="add_category"),
    path("category/<str:cats>/", CategoryView, name="category"),
    path("category-list/", CategoryListView, name="category-list"),
]
