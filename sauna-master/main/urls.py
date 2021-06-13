from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.main_page, name='main_page'),
	path('about', views.about, name='about'),
	path('calc', views.calc, name='calc'),
	path('contact', views.contact, name='contact'),
	path('designer', views.designer, name='designer')
]