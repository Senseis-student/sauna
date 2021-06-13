from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.catalog, name='catalog'),
	path('/price', views.price, name='price'),
	path('/id<int:product_id>', views.view_product, name='view_product'),
]