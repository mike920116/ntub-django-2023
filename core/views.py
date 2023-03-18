from django.shortcuts import render
from django.http import HttpResponse


def my_path(request):
    name = request.POST.get('name', 'Unknown')
    return render(request, 'my_path.html', {'name': name})


def add(request, n1, n2):
    return HttpResponse(n1 + n2)