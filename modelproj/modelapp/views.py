from django.shortcuts import render
from django.http import HttpResponse
from modelapp.models import Noobs

# Create your views here.
def register(request):
    if request.method == "POST":
        name = request.POST.get('ename')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        add = request.POST.get('add')
        NO =Noobs(name = name, pno =pno,email=email,add=add) 
        
        NO.save()
        return HttpResponse("registered succesfully")
    
    return render(request,'register.html')

def home (request):
    EO = Noobs.objects.all()
    d={'EO':EO}    
    return render(request,'home.html',d)
        