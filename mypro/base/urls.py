from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('add/<int:id>',views.add_cart,name='addcart'),
    path('de/<int:id>',views.delete,name='dlt'),
    path('cart',views.cart_page,name='cartpage'),
    path('ab',views.About,name='about'),
    path('dt/<int:id>',views.Detail,name='details'),
    
]

