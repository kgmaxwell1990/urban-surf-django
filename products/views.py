from django.shortcuts import render
from .models import Products
from django.template.context_processors import csrf


# Create your views here.
def all_products(request):
    products = Products.objects.all()
    args = {}
    args.update(csrf(request))
    return render(request, "products.html", {"products": products}, args)



