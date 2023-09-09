from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
import os



def getFileName(requset,filename):
  now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('uploads/',new_filename)
# Create your models here.


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to=getFileName,null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name 
    


class Catagory(models.Model):
  name=models.CharField(max_length=150,null=False,blank=False)
  image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  created_at=models.DateTimeField(auto_now_add=True)
 
  def __str__(self) :
    return self.name
 

 
class Product(models.Model):
  category=models.ForeignKey(Catagory,on_delete=models.CASCADE)
  name=models.CharField(max_length=150,null=False,blank=False)
  
  product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  quantity=models.IntegerField(null=False,blank=False)
  Subscriber = models.CharField(max_length=100, default='')
  Channelstatus = models.CharField(max_length=100, default='')
  Watchhour = models.CharField(max_length=100, default='')
  price = models.DecimalField(max_digits=10, decimal_places=2)
  selling_price=models.FloatField(null=False,blank=False)
  gst = models.FloatField(default=0.0)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  latest=models.BooleanField(default=False,help_text="0-default,1-Latest")
  trending=models.BooleanField(default=False,help_text="0-default,1-trending")
  
  created_at=models.DateTimeField(auto_now_add=True)


 
  def __str__(self) :
    return self.name



 

class Favourite(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)
 

class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.product_qty * self.product.selling_price
    


class transation(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.IntegerField(max_length=100)
    transationnumber=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)



class ytsell(models.Model):
    # user=models.ForeignKey(User, on_delete=models.CASCADE)
   
    ytsellname=models.CharField(max_length=100)
    Whatsapp=models.IntegerField(max_length=20)
    Channel_Link=models.CharField(max_length=1000)
    Subscribers=models.IntegerField(max_length=100)
    Status=models.CharField(max_length=100)
    Price=models.IntegerField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class ytservice(models.Model):
    # user=models.ForeignKey(User, on_delete=models.CASCADE)
   
    ytname=models.CharField(max_length=100)
    Whatsapp_number=models.IntegerField(max_length=20)
    ytChannel_Link=models.CharField(max_length=1000)
    ytSubscribers=models.IntegerField(max_length=100)
    ytStatus=models.CharField(max_length=100)
    ytPrice=models.IntegerField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)