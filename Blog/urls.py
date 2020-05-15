
from django.urls import path
from django.conf.urls import url
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    SearchResultView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='Blog-home'),
    path('search/', SearchResultView.as_view(), name='search-result'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    #path('post/<int:pk>/',views.post_detail,name='post-detail'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='Blog-about'),
    path('like/',views.like_post,name="like_post"),
]
