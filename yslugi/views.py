from django.shortcuts import render, redirect, reverse
from yslugi.models import Yslugi
from django.contrib.auth.decorators import login_required
from carts.models import Cart
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    yslugi = Yslugi.objects.all()
    
    context ={
        "yslugi": yslugi,
    }
    return render(request, 'yslugi/index.html', context)

@login_required
def kurs(request, yslugi_slug):
    kurs = Yslugi.objects.get(slug=yslugi_slug)
    cart = Cart.objects.filter(user=request.user, ysluga=kurs)
    if not cart.exists():
        return HttpResponseRedirect(reverse('yslugi:index'))
    context = {"kurs": kurs}
    return render(request, "yslugi/kurs.html", context=context)

