from django.shortcuts import render

from app.models import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        TO=Todo(title=title,description=desc)
        TO.save()
    allobj=Todo.objects.all()
    d={'allobj':allobj}
    return render(request,'index.html',d)
    
sno =0
def update(request):
    if request.method == 'GET':
        global sno
        sno=request.GET.get('pk')
        TO = Todo.objects.get(sln=sno)
        d = {'TO':TO}
        return render(request, 'update.html',d)
    elif request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        TO=Todo.objects.filter(sln=sno)
        TO.update(title=title, desc=desc)
        alltodos = Todo.objects.all()
        d = {'alltodos':alltodos}
        return render(request, 'index.html', d)

def delete(request):
    sno = request.GET.get('pk')
    TO = Todo.objects.filter(sln = sno)
    TO.delete()
    alltodos = Todo.objects.all()
    d = {'alltodos':alltodos}
    return render(request, 'index.html', d)
    
