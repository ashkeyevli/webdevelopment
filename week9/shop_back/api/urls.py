from django.contrib import admin
from api import views
from django.urls import path

urlpatterns = [
    path('categories/',views.category_list),
    path('categories/<int:pk>/', views.category_detail),
    path('categories/<int:pk>/products/', views.category_products),
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail),
    path('',views.start)
]
