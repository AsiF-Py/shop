from django.contrib import admin
from .models import * 
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','name','locality','city','zipcode','status']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','discounted','description','barnd','category']
    
@admin.register(cart)
class cartAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantiy']
@admin.register(oderplace)
class oderplaceAdmin(admin.ModelAdmin):
    list_display = ['user','product','customer','quantiy','orderd_date','status']
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
 list_display=('name','body','created','updated','active')