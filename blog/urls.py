from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    url(r'^edit-post/(?P<pk>\d+)/$', views.edit_post, name='edit_post'),
    url(r'^delete-post/(?P<pk>\d+)/$', views.delete_post, name='delete_post'),
]
