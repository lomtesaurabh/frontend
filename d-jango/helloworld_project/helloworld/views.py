# helloworld/views.py

from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    labels = ['January', 'February', 'March', 'April', 'May']
    data = [10, 20, 15, 25, 30]

    context = {
        'labels': labels,
        'data': data,
    }

    return render(request, 'hello_world.html', context)
