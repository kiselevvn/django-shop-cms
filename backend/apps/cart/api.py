from django.urls import path
from .programming_interface import (
    AddProductToCart,
    DestroyProductCart,
    UpdateСountProduct,
)

urlpatterns = [
    path("add-product-to-cart/", AddProductToCart.as_view()),
    path("destroy-product-cart/<int:pk>/", DestroyProductCart.as_view()),
    path("update-count-product/<int:pk>/", UpdateСountProduct.as_view()),
]
