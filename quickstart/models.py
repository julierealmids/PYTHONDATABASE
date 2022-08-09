from django.db import models

# Create your models here.


class Categories(models.Model):
      category_Id=models.IntegerField(primary_key=1)
      quantity=models.BigIntegerField(blank=True)
      name=models.CharField(max_length=25,blank=True)
      description=models.TextField(max_length=50,blank=True)
      def __str__(self) -> str:
            return self.name



class Product(models.Model):
       product_Id=models.IntegerField(primary_key=2)
       category_Id=models.ForeignKey(Categories,on_delete=models.CASCADE)
       size=models.SmallIntegerField()
        # name_id=models.SmallIntegerField(default=2)
       name=models.CharField(max_length=20,blank=True)
       brand=models.CharField(max_length=20)
       image=models.ImageField(blank=True)
       quantity_in_stock=models.BigIntegerField(blank=True)
       color=models.CharField(max_length=20,null=True)
       price=models.IntegerField(default=1)
       type=models.CharField(max_length=20)
       def __str__(self) -> str:
            return self.name
                
        
class Cart(models.Model):
    cart_Id=models.IntegerField(primary_key=3)
    user_id=models.IntegerField(default=1)
    number_of_products=models.IntegerField(blank=True)
    def __str__(self):
            return self.name
    
class CartItem(models.Model):
    cartItem_Id=models.IntegerField(primary_key=4)
    name=models.ForeignKey(Product,on_delete=models.CASCADE)
  # image=models.ImageField(Product,on_delete=models.CASCADE)
    cart_Id=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.BigIntegerField(blank=True)
    def __str__(self):
        return self.name
    