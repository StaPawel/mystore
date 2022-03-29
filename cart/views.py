from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from .forms import Cart
from django.http import HttpResponseRedirect
from products.forms import ProductForm

from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)
from django.urls import reverse

from products.models import Products
from .models import Cart

cartProductsId = []

def getCart(request):
    cart = Cart.objects.get(customer_id=request.user.id)
    return cart

def cart_detail_view(request):

    isCartEmpty = False
    cart = Cart.objects
    productCart = []

    form = ProductForm()
    if form.is_valid():
            form.save()

    if Cart.objects.filter(customer_id=request.user.id):
        isCartEmpty = True
        cart = getCart(request)
        productCart = list(cart.products.all())
        request.session['cartlen'] = len(productCart)

    context = {
        "is_cart_empty": isCartEmpty,
        "object_list": productCart,
        "cart_sum": cart,
        "form": form
    }
    return render(request, "cart_detail.html", context)

def cart_add(request):
    productId = int(request.COOKIES['productId'])
    product = Products.objects.get(id=productId)

    # cart = Cart.objects.get(customer_id=request.user.id)
    cart = Cart()

    if Cart.objects.filter(customer_id=request.user.id):
        cart = Cart.objects.get(customer_id=request.user.id)
        cart.products.add(product)
        cart.sum = cart.sum + product.price
        cart.save()
    else:
        cart = Cart(sum=product.price, customer_id=request.user.id)
        cart.save()
        cart.products.add(product)
        cart.save()

    return HttpResponseRedirect('/products/'+str(productId))

def cart_delete(request):
    productId = int(request.COOKIES['productId'])
    cart = Cart.objects.get(customer_id=request.user.id)
    # cart.products.add(Products.objects.get(id=productId))
    cart.products.remove(Products.objects.get(id=productId))
    return HttpResponseRedirect('/cart')



