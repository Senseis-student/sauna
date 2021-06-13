from django.shortcuts import render, reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from . import models

# Create your views here.
def blog_list(request):
	a = models.Article.objects.order_by('-id')
	return render(request, 'blog/list.html', {'list':a})

def view_post(request, post_id):
    post = models.Article.objects.get(id=post_id)
    post_list = models.Article.objects.exclude(id=post_id).order_by('-id')[0:3]
    return render(request, 'blog/index.html',{'post':post,'post_list':post_list})