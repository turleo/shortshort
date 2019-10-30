from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse

from .models import Link

# Create your views here.

def goto(request, id):
	return redirect(get_object_or_404(Link, short=id).long, request)


def new_from_api(request):
	obj = Link.objects.create(long = request.GET.get('q', ''))
	obj.short = hex(obj.id).split('x')[-1]
	obj.save()
	return HttpResponse(hex(obj.id).split('x')[-1])


def index_file(request):
	return render (request, 'index.html')
	