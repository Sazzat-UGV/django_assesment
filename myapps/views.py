from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def print_response(request):
    return HttpResponse("<h1>Hello I am Sazzat</h1>")
