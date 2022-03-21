from django.urls import path
from .views import (
    # CartDetailView,
    cart_detail_view,
    cart_popup_view,
    cart_delete

)

app_name = 'cart'
urlpatterns = [
    # path('<int:id>/', CartDetailView.as_view(), name='cart-detail'),
    path('', cart_detail_view, name='cart-detail'),
    path('add', cart_popup_view, name='cart-popup'),
    path('delete', cart_delete, name='cart-delete'),
]