
from . import views
from django.urls import path

urlpatterns = [
    path("", views.cart_summary, name="cart_summary"),
    path("cart_add", views.cart_add, name="cart_add" ),
    path("cart_update", views.cart_update, name="cart_update" ),
    path("cart_delete", views.cart_delete, name="cart_delete" ),
    
   

]
