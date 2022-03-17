from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from cart.models import *
# from .models import *
def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id
def cart_Details(request,tot=0,ct_items=None,count=0):
    try:
        ct=cartlist.objects.get(cartid=c_id(request))
        ct_items=items.objects.filter(cartss=ct,active=True)
        for i in ct_items:
            tot += i.prodt.price * i.quantity
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count})

def add_cart(request,product_id):
    prod=products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cartid=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cartid=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prodt=prod,cartss=ct)
        if c_items.quantity < c_items.prodt.stock:
            c_items.quantity+=1
            c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prod,quantity=1,cartss=ct)
        c_items.save()
    return redirect('cartDetails')
def min_cart(request,product_id):
    ct=cartlist.objects.get(cartid=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prod,cartss=ct)
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')
def cart_delete(request,product_id):
    ct = cartlist.objects.get(cartid=c_id(request))
    prod = get_object_or_404(products, id=product_id)
    c_items = items.objects.get(prodt=prod, cartss=ct)
    c_items.delete()
    return redirect('cartDetails')
def logout(request):
    auth.logout(request)
    return redirect('/')


