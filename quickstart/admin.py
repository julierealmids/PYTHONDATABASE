from email.mime import image
from itertools import product
from pyexpat import model
from unicodedata import category, name
from unittest.util import _MAX_LENGTH
from django.contrib import admin
from django.db import models

from quickstart.models import Cart, CartItem, Categories,Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Cart)
admin.site.register(CartItem)
    

    
