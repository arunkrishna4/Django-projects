from django.http import HttpResponse
from django.shortcuts import render
from app.models import *
# Create your views here.
def registration(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        pno=request.POST.get('pno')
        un=request.POST.get('un')
        pw =request.POST.get('pw')
        cpw =request.POST.get('cpw')
        if pw == cpw:
            DO=Details(name=name,pno=pno,un=un,pw=pw)
            DO.save()
            return HttpResponse('registration succesful')
        return HttpResponse('password did not match')
    
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')