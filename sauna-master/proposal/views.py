from django.shortcuts import render, reverse, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from . import models


def proposal(request):
    if request.method =='GET':
        form = models.Options.objects.all()
        return render(request, 'proposal/index.html', {})
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        scale = request.POST['scale']
        sity = request.POST['sity']
        village = request.POST['village']
        number = request.POST['number']
        email = request.POST['email']
        form_options = request.POST['form_options']
        img = request.POST['img']
        a = models.Form()
        a.name = name
        a.description = description
        a.scale = scale
        a.sity = sity
        a.village = village
        a.number = number
        a.email = email
        a.form_options = form_options
        a.img = img
        if a.number!='':
            if a.email!='':
                a.save()
    return redirect ('proposal')