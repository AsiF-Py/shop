from django.shortcuts import render , redirect , get_object_or_404
from .models import Product , cart
from django.db.models import Avg,Sum,Max,Min,Count
from django.views.generic import ListView , DetailView
from .models import Comment, Customer
from django.views.generic.edit import FormMixin
from .forms import CommentForm , CustomerForm,oderplaceForm
from django.urls import reverse

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    save_cart = cart(user=user,product=product)
    save_cart.save()
    return redirect('/cart/')
    # return render(request,'cart.html')
def show_cart(request):
    total = cart.objects.annotate(Count('product'))
    print(total)
    if request.user.is_authenticated:
        user = request.user
        itam = cart.objects.filter(user=user)
        return render(request,'cart.html',{'itams':itam,'sum':sum,'total':total})   



def delete_cart_item(request,id):
    itam =  cart.objects.get(id=id)
    itam.delete()
    return redirect("/cart")           

def product_view(request):
    product_list = Product.objects.all()
    return render(request,'app/product_list.html',{'product_list':product_list})

def product_detail(request,barnd,product):
    product = get_object_or_404(Product,slug=product)
    comments=product.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(data=request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.product=product
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()
    return render(request,'app/product_detail.html',{'form':form,'csubmit':csubmit,'product':product,'comments':comments})




def profile(request):
    user = request.user
    customer=Customer.objects.filter(user=user)
    form=CustomerForm()
    csubmit=False
    if request.method=="POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            # form = Customer(user=user)
            form.save()
            csubmit=True
    return render(request,'account.html',{'form':form,'csubmit':csubmit,'customer':customer})


