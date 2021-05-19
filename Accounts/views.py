from django.shortcuts import render

# Create your views here.
def home(requset):
    return render(requset,'home.html')
def content(request):
    return render(request,'content.html')