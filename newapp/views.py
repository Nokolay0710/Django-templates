from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def list(request):
    return render(request, 'list.html')

def add(request):
    return render(request, 'add.html')

