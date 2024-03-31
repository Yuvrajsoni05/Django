from django.shortcuts import render, redirect
from .models import UserName

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        UserName.objects.create(name=name)
        return redirect('success')
    return render(request, 'index.html')

def success(request):
    names = UserName.objects.all()
    return render(request, 'show.html', {'names': names})
