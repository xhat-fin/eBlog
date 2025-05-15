from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post

# Create your views here.

def all_posts(request):
    posts = Post.objects.exclude(deleted_at__isnull=False)
    posts_pagination = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = posts_pagination.get_page(page_number)
    print([i for i in posts_pagination])
    print(page_obj)
    data = []
    for post in posts:
        data.append({
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "created_at": post.created_at,
            "updated_at": post.updated
        })

    return render(request, 'view_posts.html', {"page_obj":page_obj})

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
        return render(request, 'view_post_by_id.html', {"data": data})
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Not Found"}, status=404)


def index(request):
    return render(request, 'index.html')


def create_post(requst):
    pass