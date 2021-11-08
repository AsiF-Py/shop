from django.db import models
from django.db.models.enums import Choices
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

STATE_CHOIES = (('hathazari','Hathazari'),
        ('forhadabad','Forhadabad'),
        ('katirhat','Katirhat'),
        ('nazirhat','Nazirhat'),
    
)
class Customer(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    status = models.CharField(max_length=50,choices=STATE_CHOIES)
    image = models.ImageField(null=True,upload_to='profile_Pic/',blank=True)         
    def __str__(self):
        return str(self.id)


STATE_CHOIES1 = (('L','Loptop'),
        ('M','Mobile'),
        ('P','Pants'),
        ('T','T-shart'),
)
class Product(models.Model):
    title = models.CharField(max_length=50)
    slug =  models.SlugField(max_length=40)
    price = models.IntegerField()
    discounted = models.IntegerField()
    description = models.TextField()
    barnd = models.CharField(max_length=50)
    category = models.CharField(choices=STATE_CHOIES1,max_length=50,)
    image =  models.ImageField(upload_to='myimg')
    tags=TaggableManager()
    def __str__(self):
        return str(self.id)
    def get_absolute_url(self):
        return reverse("product_detail",args=[self.barnd,self.slug])    
    # def get_absolute_url(self):
    #     return reverse("ProductDetailView", kwargs={"pk": self.pk})
        

class cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantiy =models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
  
STATE_CHOIES2 = (('Accepted','Accepted'),
        ('Packed','Packed'),
        ('On The Wey','On The Wey'),
        ('Delivered','Delivered'),
        ('Cancal','Cancal')
)        
class oderplace(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantiy =models.PositiveIntegerField(default=1)   
    orderd_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATE_CHOIES2,max_length=50,default='Pending')

class Comment(models.Model):
    product=models.ForeignKey(Product,related_name='comments',on_delete=models.CASCADE,blank=True, null=True)
    name=models.ForeignKey(User,max_length=32,on_delete=models.CASCADE,blank=True, null=True)
    # email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=('created',)
    def __str__(self):
        return 'Commented By {} on {}'.format(self.name,self.product)    

