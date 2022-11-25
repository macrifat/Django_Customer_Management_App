from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()
    total_customer = customer.count()
    total_order = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    diction = {'orders': orders, 
               'customers': customer, 
               'total_customer':total_customer,
               'total_order': total_order,
               'delivered': delivered,
               'pending': pending
               }
    return render(request, 'myapp/dashboard.html', context=diction)

def product(request):
    product= Product.objects.all()
    diction = {'products':product}
    return render(request, 'myapp/product.html',context= diction)

def customer(request):
    return render(request, 'myapp/customer.html')
