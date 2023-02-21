from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductFroms
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

def product_create(request):
    form=ProductFroms()
    if request.method=="POST":
        form=ProductFroms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={
        "form":form
    }
    return render(request,"products/product_create.html",context)

def product_update(request, pk):
    product=Product.objects.get(id=pk)
    form=ProductFroms(request.POST or None, instance=product)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect("/")
    context={
        "form":form
    }
    return render(request,"products/product_create.html",context)

def product_delete(request,pk):
    product=Product.objects.get(id=pk)
    if request.method=="POST":
        product.delete()
        return redirect('/')
    return render(request,"products/product_delete.html")