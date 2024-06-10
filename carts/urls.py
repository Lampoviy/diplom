from django.urls import path
from carts import views

app_name = "cart"

urlpatterns = [
    path("yslugi_add/<slug:yslugi_slug>", views.yslugi_add, name= 'yslugi_add'),
    path("yslugi_remove/<int:cart_id>", views.yslugi_remove, name= 'yslugi_remove'),
]