from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from carts.models import Cart
from yslugi.models import Yslugi
from django.contrib.auth.decorators import login_required


def yslugi_add(request, yslugi_slug):
    yslugi = Yslugi.objects.get(slug=yslugi_slug)
    
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, ysluga=yslugi)
        
        if carts.exists():
            cart = carts.first()
            if cart:
                messages.success(request, "Вы купили курс")  
                return HttpResponseRedirect(reverse('user:profile'))
        else:
            Cart.objects.create(user=request.user, ysluga=yslugi)
            messages.success(request, "Вы записались")  
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        messages.success(request, "Пожалуйста войдите в аккаунт")  
        return HttpResponseRedirect(reverse('user:login'))  

           
      


def yslugi_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    messages.success(request, "вы отменили запись") 
    return redirect(request.META['HTTP_REFERER'])
