from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('post_detail/<int:blog_id>/', views.PostDetail.as_view(), name='post_detail'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:blog_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:blog_id>/', views.delete_post, name='delete_post'),
    path('like/like_post/<int:blog_id>/', views.like_post, name='like_post'),
]
