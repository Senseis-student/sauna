from django.shortcuts import render, reverse
from . import models
from proposal.models import Options
from django.http import Http404, HttpResponseRedirect, HttpResponse

# Create your views here.
def project(request):
	projects = models.Project.objects.all()
	options = Options.objects.all()
	return render(request, 'project/index.html', {'projects': projects, 'options':options})

