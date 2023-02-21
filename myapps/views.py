from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def print_response(request):
    return HttpResponse("<h1>Hello I am Sazzat</h1>")

def product_list(request):
    product=Product.objects.all()
    context={
        'product':product
    }
    return render(request,"products/product_list.html",context)

def product_detail(request ,pk):
    product=Product.objects.get(id=pk)
    context={
        'product':product
    }
    return render(request,"products/product_details.html",context)

