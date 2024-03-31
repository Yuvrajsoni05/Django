from django.shortcuts import render

# Create your views here.

def sign(request):
    return render(request,"signdetail/sign.html")