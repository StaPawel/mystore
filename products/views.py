from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .forms import ProductForm

from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)
from django.urls import reverse
from .models import Products


class ProductsListView(ListView):
    template_name = 'products_list.html'
    queryset = Products.objects.all()

class ProductsDetailView(DetailView):
    template_name = 'products_detail.html'
    queryset = Products.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        print("Product Id from product detail view:" + str(id_))

        return get_object_or_404(Products, id=id_)

# ponizej rozwiazanie dla kilku contex
# class ProductsDetailView(generic.DetailView):
#     model = Products
#     template_name = 'products_detail.html'
#
#     # def get_context_data(self, **kwargs):
#     #     form = ProductForm()
#     #     if form.is_valid():
#     #         form.save()
#     context = super().get_context_data(**kwargs)
#     context['object'] = Products.objects.all()
#         # context['form'] = form
#     return context

# def get_name(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     context = {
#         'form': form
#     }
#     return render(request, 'products_detail.html', context)

# def new_measurement(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     qs = Products.objects.all()
#     context = {'form': form, 'qs': qs}
#     return render(request, 'products_detail.html', context)

# class ProductsDetailView(DetailView):
#     template_name = 'products_detail.html'
#     queryset = Products.objects.all()
#
#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         print("Product Id from product detail view:" + str(id_))
#
#         return get_object_or_404(Products, id=id_)# def new_measurement(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     qs = Products.objects.all()
#     context = {'form': form, 'qs': qs}
#     return render(request, 'products_detail.html', context)

# class ProductsDetailView(DetailView):
#     template_name = 'products_detail.html'
#     queryset = Products.objects.all()
#
#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         print("Product Id from product detail view:" + str(id_))
#
#         return get_object_or_404(Products, id=id_)
