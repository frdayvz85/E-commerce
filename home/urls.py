from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.about, name='aboutus'),
    path('contact', views.contact, name='contact'),
    path('search/', views.product_search, name='product_search'),
    path('faq/', views.faq, name='faq'),
    path('search_auto/', views.product_search_auto, name='product_search_auto'),
    path('category/<int:id>/<slug:slug>/', views.category_products, name='category_products'), 
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail') ,
    
]