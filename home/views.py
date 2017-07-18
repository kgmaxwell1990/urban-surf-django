from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

# Create your views here.
def get_index(request):
    return render(request, 'index.html')

def top3_post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')[0:3]
    return render(request, "index.html", {'posts': posts})