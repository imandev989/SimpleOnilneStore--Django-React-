from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Product(models.Model):
    """Model definition for Product."""
    


    # TODO: Define fields here
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(blank=True, null=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    # def __str__(self):
    #     """Unicode representation of Product."""
    #     pass
    

class Review(models.Model):
    """Model definition for Review."""

    # TODO: Define fields here
    _id = models.AutoField(primary_key=True, editable=False)
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Review."""

        verbose_name = 'بازدید'
        verbose_name_plural = 'بازدیدها'

    # def __str__(self):
    #     """Unicode representation of Review."""
    #     pass



class Order(models.Model):
    """Model definition for Order."""

    # TODO: Define fields here
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    isPaid= models.BooleanField(default=False)
    isDelivered= models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        """Meta definition for Order."""

        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    # def __str__(self):
    #     """Unicode representation of Order."""
    #     pass



class OrderItem(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    _id = models.AutoField(primary_key=True, editable=False)
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'آیتم سفارش'
        verbose_name_plural = 'آیتمهای سفارش'

    # def __str__(self):
    #     """Unicode representation of MODELNAME."""
    #     pass



class ShippingAddress(models.Model):
    """Model definition for ShippingAddress."""

    # TODO: Define fields here
    _id = models.AutoField(primary_key=True, editable=False)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True,blank=True)
    posttalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    class Meta:
        """Meta definition for ShippingAddress."""

        verbose_name = 'آدرس سفارش'
        verbose_name_plural = 'آدرس سفارشات'

    # def __str__(self):
    #     """Unicode representation of ShippingAddress."""
    #     pass
