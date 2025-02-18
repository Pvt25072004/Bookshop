from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def ImageURL(self):
        try:
            return self.image.url
        except ValueError:
            return ''

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    finish = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_items(self):
        return sum(item.quantity for item in self.orderitem_set.all())

    @property
    def get_cart_total(self):
        return sum(item.get_total for item in self.orderitem_set.all())

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    date_bought = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.product.price * self.quantity

class InfoAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    commune = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)
    date_bought = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
