from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'myapp/dashboard.html')

def product(request):
    return render(request, 'myapp/product.html')

def customer(request):
    return render(request, 'myapp/customer.html')
