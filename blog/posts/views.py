from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Post

# Create your views here.

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Создать пост", "url_name": "create_post"},
    {"title": "Поиск", "url_name": "search"},
    {"title": "Просмотреть все посты", "url_name": "all_posts"},
]

def all_posts(request):
    posts = Post.objects.exclude(deleted_at__isnull=False)
    posts_pagination = Paginator(posts, 5)
    page_number = request.GET.get('page')

    if page_number is not None and (int(page_number) > int(posts_pagination.num_pages)):
        return redirect('all_posts')

    page_obj = posts_pagination.get_page(page_number)
    data = []
    for post in posts:
        data.append({
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "created_at": post.created_at,
            "updated_at": post.updated
        })

    return render(request, 'posts/view_posts.html', {"page_obj":page_obj, "menu": menu})

def post_by_id(request, id):
    try:
        post = Post.objects.exclude(deleted_at__isnull=False).get(id=id)
        data = {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "created_at": post.created_at,
            "updated_at": post.updated
        }
        return render(request, 'posts/view_post_by_id.html', context={"data": data, "menu": menu})
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Not Found"}, status=404)


def index(request):

    return render(request, 'posts/index.html', context={"menu": menu})


def create_post(request):
    return HttpResponse("<h1 align='center'>CREATE POST</h1>")


def about(request):
    return HttpResponse("<h1 align='center'>ABOUT </h1>")



def search(request):
    return HttpResponse("<h1 align='center'>SEARCH POST</h1>")
