from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # User.objects.create(name=name)

        return render(request, 'index.html', {'name': name})
    return render(request, 'index.html')

