from django.shortcuts import render, reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse

# Create your views here.
def reviews(request):
	return render(request, 'reviews/index.html')