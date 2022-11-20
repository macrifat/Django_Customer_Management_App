from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home),
    path('product/',views.product),
     path('customer/',views.customer),
    
]