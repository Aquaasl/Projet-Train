from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "projettrain\train\templates\index.html", {})

def compte(request):
    return render(request, "projettrain\train\templates\compte.html", {})

def liste(request):
    return render(request, "projettrain\train\templates\liste.html", {})

