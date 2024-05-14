from django.shortcuts import render

# Create your views here.
def signup(request):
    if request.method == "POST":
        name = request.POST.get('ename')
        
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

