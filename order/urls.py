from django.urls import path

from .import views

urlpatterns = [
    path('', views.order, name='order'),
    path('addtocart/<int:id>', views.addtocart, name='addtocart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    
]