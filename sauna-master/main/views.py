from django.shortcuts import render, reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from . import models

def main_page(request):
	businessMap = models.Map.objects.get()
	return render(request, 'main/index.html', {'businessMap':businessMap})

def about(request):
	return render(request, 'main/about.html')

def calc(request):
	return render(request, 'main/calc.html')

def contact(request):
	return render(request, 'main/contacts.html')

def designer(request):
	return render(request, 'main/designer.html')