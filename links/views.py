from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse

from .models import Link


def goto(request, short: str):
    pk = 0
    for i, symbol in enumerate(short):
        pk += settings.BASE_SYMBOLS.index(symbol) * (settings.BASE ** i)
    link = get_object_or_404(Link, pk=pk)
    return redirect(link.long, request)


def new_from_api(request):
    obj = Link.objects.create()
    obj.long = request.GET.get('q', '')
    obj.save()
    return HttpResponse(bytes(obj.short(), 'utf8'))


def index_file(request):
    return render(request, 'index.html')


def file_404(request, exception):
    return render(request, 'oops.html', status=404)
