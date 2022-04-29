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

    quantityProductId = int(request.COOKIES['quantityProductId'])
    quantity = int(request.COOKIES['quantity'])

    print(quantityProductId)
    print(quantity)

    # Zastanwic sie czy nie lepiej bedzie jesli ponizsze rozwiazanie bedzie robione
    # w javascript (cart.js) zamiast w django. W samym django tylko pobranie quantity
    # 1. pobierz id produktu z cookie
    # 2. pobierz wszystkie id produktow z koszyka i porownaj je z id z punktu nr. 1
    # 3. jesli quantityProductId == id produktu to
    #       quantity produktu == quantity z cookie
    # 4. przypisz quantity do odpowiedniego pola

    if Cart.objects.filter(customer_id=request.user.id):
        isCartEmpty = True
        cart = getCart(request)
        productCart = list(cart.products.all())
        request.session['cartlen'] = len(productCart)

        print(productCart)
        for product in productCart:
            print(product.quantity)

        sum = cart.sum * quantity

    context = {
        "is_cart_empty": isCartEmpty,
        "object_list": productCart,
        "cart_sum": sum,
        "form": form,
        "quantity": quantity
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



