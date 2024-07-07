from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):

    STATUS_CHOICES = (
        ("Active", 'active'),
        ("In-Active", 'inactive'),
        )
    
    id           = models.AutoField(primary_key=True,db_index=True)                                   
    status       = models.CharField(choices=STATUS_CHOICES,default="Active",max_length=100)
    created_at   = models.DateTimeField(auto_now_add=True)                                            
    updated_at   = models.DateTimeField(auto_now=True)                                                

    class Meta:
        abstract = True


class ProductMstModel(BaseModel):
    code = models.CharField(max_length=1000,verbose_name="Product Code")
    desc = models.CharField(max_length=1000,verbose_name="Product Desc")
    price = models.CharField(max_length=1000,verbose_name="Price")
    category = models.CharField(max_length=1000,verbose_name="Product Category")
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.desc

class ShoppingCartModel(BaseModel):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    product = models.ForeignKey(ProductMstModel,on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    is_ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.desc

class PaymentsModel(BaseModel):
    payment_amount = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    utr_no = models.CharField(max_length=1000,verbose_name="UTR")
    payment_datetime = models.DateTimeField()


class AddressModel(BaseModel):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    address_line = models.CharField(max_length=1000,verbose_name="Address line")
    city = models.CharField(max_length=500,verbose_name="City")
    state = models.CharField(max_length=500,verbose_name="State")
    country = models.CharField(max_length=500,verbose_name="Country")
    pincode = models.CharField(max_length=500,verbose_name="Pincode")


class OrderModel(BaseModel):
    product = models.ForeignKey(ProductMstModel,on_delete=models.PROTECT)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    payment = models.ForeignKey(PaymentsModel,on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.ForeignKey(AddressModel,on_delete=models.PROTECT)

