from django.urls import path

from .views import (
    ProductsListView,
    ProductsDetailView,
)
app_name = 'products'
urlpatterns = [
    path('', ProductsListView.as_view(), name='products-list'),
    path('<int:pk>/', ProductsDetailView.as_view(), name='products-detail'),
    # path('aaa', cart_popup_view, name='add-to-cart'),
]