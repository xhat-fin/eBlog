from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.all_posts, name='all_posts'),
    path('posts/<int:id>/', views.post_by_id, name='post_by_id'),
    path('about/', views.about, name='about'),
    path('create-post/', views.create_post, name='create_post'),
    path('search/', views.search, name='search'),
]
