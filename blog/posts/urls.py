from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.all_posts, name='all_posts'),
    path('posts/<int:id>/', views.post_by_id, name='post_by_id'),
]
