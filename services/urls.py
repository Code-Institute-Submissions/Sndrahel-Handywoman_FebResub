from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('construction/', views.construction, name='construction'),
    path('logistic/', views.logistic, name='logistic'),
    path('mechanics/', views.mechanics, name='mechanics'),
    path('webb/', views.webb, name='webb'),
    path('law/', views.law, name='law'),
    path('other/', views.other, name='other'),
]
