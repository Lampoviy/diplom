from django.urls import path
from yslugi import views

app_name = "yslugi"

urlpatterns = [
    path("index", views.index, name= 'index'),
    path('<slug:yslugi_slug>/', views.kurs, name='kurs'),
]