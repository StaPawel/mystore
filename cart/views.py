from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import Cart
from django.http import HttpResponseRedirect


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

def cart_detail_view(request):
    # rozwiazanie z pusta lista ---------------------
    # productId = int(request.COOKIES['productId'])
    # objList = []
    #
    # if not productId in cartProductsId:
    #     cartProductsId.append(productId)
    #
    # for product in cartProductsId:
    #     objList.append(Products.objects.get(id=product))
    # ---------------------

    # cart = Cart.objects.all().filter(customer=request.user.id) #typ -> QuerySet
    cart = Cart.objects.get(customer_id=request.user.id) # typ -> models.Cart
    # cart = Cart.objects.all()
    productCart = list(cart.products.all())
    request.session['cartlen'] = len(productCart)

    # print(Cart.objects.get(id=1))
    # cart = Cart.objects.get(id=1)
    # print(Cart.objects.all())
    # print(cart.products.all())
    # print(request.user.id)


    context = {
        "object_list": productCart,
        "cart_sum": cart
    }
    return render(request, "cart_detail.html", context)

def cart_popup_view(request):
    productId = int(request.COOKIES['productId'])
    cart = Cart.objects.get(customer_id=request.user.id)
    product = Products.objects.get(id=productId)
    cart.products.add(product)
    cart.sum = cart.sum + product.price
    cart.save()
    return HttpResponseRedirect('/products/'+str(productId))

def cart_delete(request):
    productId = int(request.COOKIES['productId'])
    cart = Cart.objects.get(customer_id=request.user.id)
    # cart.products.add(Products.objects.get(id=productId))
    cart.products.remove(Products.objects.get(id=productId))
    return HttpResponseRedirect('/cart')

# ponizej class view. Zamienic cart_detail_view na class??
# class CartBasket(ListView):
#     template_name = 'cart_detail.html'
#     def get_queryset(self):
#         queryset = Cart.objects.all().filter(customer=self.request.user.id)
#         print("in class view")



