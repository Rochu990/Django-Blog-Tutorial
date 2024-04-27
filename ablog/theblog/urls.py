from django.urls import path

# from . import views
from .views import ArticleDetailView, HomeViev, AddPostView, UpdatePostView, DeletePostView, AddCategoryView

urlpatterns = [
    # path("", views.home, name="home")
    path("", HomeViev.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path("add_post/", AddPostView.as_view(), name='add_post'),
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name='update-post'),
    path("article/<int:pk>/remove", DeletePostView.as_view(), name='delete-post'),
    path("add_category/", AddCategoryView.as_view(), name='add_category'),
]
