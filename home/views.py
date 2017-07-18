from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
def get_index(request):
    return render(request, 'index.html')

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})

def top3_post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')[0:3]
    return render(request, "index.html", {'posts': posts})