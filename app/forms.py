from .models import Comment,Customer,oderplace
from django import forms
class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields=('name','body')
class CustomerForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields=('image','user','name','locality','city','zipcode','status')  
class oderplaceForm(forms.ModelForm):
    class Meta:
        model= oderplace
        fields=('user','product','customer','quantiy','status')  
               