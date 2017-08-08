from django.shortcuts import render, get_object_or_404
from products.models import Products

# Create your views here.

def do_search(request):
    products = Products.objects.filter(name__contains=request.GET['q'])
    return render(request, 'results.html', {'Products': products})


