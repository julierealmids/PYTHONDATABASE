from django.shortcuts import render
from product.models import Categories, Product, Cart, CartItem
from rest_framework import viewsets
from product.serializer import Categoriesserializer,Productserializer,Cartserializer,CartItemserializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = Productserializer
    
class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all().order_by('name')
    serializer_class = Categoriesserializer
    
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = Cartserializer
    
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemserializer
















