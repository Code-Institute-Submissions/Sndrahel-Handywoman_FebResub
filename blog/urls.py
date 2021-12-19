from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
