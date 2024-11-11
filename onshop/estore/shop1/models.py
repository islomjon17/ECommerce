from django.db import models

# Create your models here.
import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories list"


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    class Meta:
        verbose_name_plural = "Customers list"

    
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    description = models.CharField(max_length=255, default='', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default=1, related_name='products')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="uploads/product/")
    is_sale = models.BooleanField(default=False)
    sale_price =  models.DecimalField(default=0, decimal_places=2, max_digits=6)
    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Products list"

    def __str__(self):
        return self.name
    
#Customer orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pustomer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone =  models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.product
    
    class Meta:
        verbose_name_plural = "Orders list"