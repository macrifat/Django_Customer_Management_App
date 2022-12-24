from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

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

def customer(request,pk):
    customer= Customer.objects.get(id=pk)
    orders= customer.order_set.all()
    order_count= orders.count()
    
    diction= {'customer': customer,
             'orders':orders,
             'order_count':order_count
             }
    
    return render(request, 'myapp/customer.html', context= diction)

def createOrder(request):
    form = OrderForm()
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'myapp/order_form.html',context)


def updateOrder(request,pk):
    order = Order.objects.get(id = pk)
    form = OrderForm(instance=order)
    
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'myapp/order_form.html', context)

def deleteOrder(request, pk):
    order= Order.objects.get(id=pk)
    
    if request.method == "POST":
        order.delete()
        return redirect('/')
    
    context = {'item': order}
    return render(request, 'myapp/delete_order.html', context)