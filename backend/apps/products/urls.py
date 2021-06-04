from django.urls import include, path
from .views import ProductList, ProductDetail

urlpatterns = [
    path("", ProductList.as_view(), name="product-list"),
    path("<int:pk>/", ProductDetail.as_view(), name="product-detail"),
]
