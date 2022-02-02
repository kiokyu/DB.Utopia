from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={})

def res(request):
    return render(request, 'res.html', context={})

