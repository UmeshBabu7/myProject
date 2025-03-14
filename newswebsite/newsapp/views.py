from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'newsapp/index.html')

def politics(request):
    return render(request,'newsapp/politics.html')

def sports(request):
    return render(request,'newsapp/sports.html')


def entertainment(request):
    return render(request,'newsapp/entertainment.html')