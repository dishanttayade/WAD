from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'manager/index.html')

def signup(request):
    return render(request,'manager/signup.html')

def login(request):
    return render(request,'manager/login.html')

def blog(request):
    return render(request,'manager/blog.html')

def myaccount(request):
    return render(request,'manager/myaccount.html')