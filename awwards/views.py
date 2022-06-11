from django.shortcuts import render


def homepage(request):
   
    return render(request,"awwards/homepage.html")
# Create your views here.
