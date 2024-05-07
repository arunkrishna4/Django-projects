from django.http import HttpResponse
from django.shortcuts import render

from app.forms import ModelRegisterForm
from app.models import Register

# Create your views here.
def register(request):
    EMRFO = ModelRegisterForm()
    d = {'EMRFO':EMRFO}
    if request.method == 'POST':
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        add = request.POST.get('add')
        gender = request.POST.get('gender')
        course = request.POST.get('cource')
        un = request.POST.get('username')
        pw = request.POST.get('password')
        TRO = Register(name = name, pno = pno, email = email, add = add, gender = gender, cource=course, username = un, password = pw)
        TRO.save()
        return HttpResponse('Done')
    return render(request, 'register.html', d)