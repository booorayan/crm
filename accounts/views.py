from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'customers': customers, 'orders': orders,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}

    return render(request, 'dashboard.html', context)


def products(request):
    productss = Product.objects.all()

    context = {'products': productss}

    return render(request, 'products.html', context)


def customer(request, pk):
    kastama = Customer.objects.get(id=pk)

    orders = kastama.order_set.all()
    orders_count = orders.count()

    context = {'customer': kastama, 'orders': orders, 'orders_count': orders_count}

    return render(request, 'customer.html', context)
