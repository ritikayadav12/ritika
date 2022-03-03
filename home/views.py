from django.shortcuts import render
from django .http import HttpResponse

def index(request):
    return render(request,"index.html")

def menu(request):
   return render(request,'menu.html')
   #return HttpResponse("this is about page")

def offers(request):
 return render(request,'offers.html')