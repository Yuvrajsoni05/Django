from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect



def index(request):
    return render(request, 'index.html')

def display_data(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', )
        send_mail(
            'User Data Submission',
            f'User Name: {user_name}',
            settings.DEFAULT_FROM_EMAIL,
            ['yuvrajsoni9192@gmail.com'],  # Replace with your actual email address
            fail_silently=False,
        )
        return render(request, 'display_data.html', {'user_name': user_name})
    else:
        return HttpResponseRedirect('/')

