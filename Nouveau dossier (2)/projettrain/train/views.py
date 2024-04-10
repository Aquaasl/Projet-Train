from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"train/template/acceuil.html", ())

def compte(request):
    return render(request,"train/template/login.html" ())

def liste(request):
    return render(request, "train/template/liste_train.html")


