from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User

from .models import StudentUser

# from django.contrib.auth.models import cr_student
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'index.html')


def adminLogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('adminHome')
        else:
            return HttpResponse("User Name Or Password incorrect")


    return render(request,'admin_side/login.html')


@login_required(login_url='adminLogin')
def adminSignup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password2')


        if pass1 != pass2:
            return HttpResponse("Password Will Be Not Same ")
        else:
            admin_user = User.objects.create_user(uname, email, pass1)
            admin_user.save()
            # return HttpResponse("User Hase Been Created")
            return redirect('adminLogin')



    return render(request,'admin_side/signup.html')


@login_required(login_url='adminLogin')
def adminHome(request):
    return render(request, 'admin_side/home.html')
@login_required(login_url='adminLogin')
def adminLogout(request):
    logout(request)
    return redirect('adminLogin')


# Student Side
def studentsignup(request):
    # if request.method == 'POST':
    #     name = request.POST.get('crname')
    #     StudentUser.objects.create(name=name)
    #     return redirect('studentlogin')
    # else:
    #     user_data = StudentUser.objects.all()
    return render(request, 'student_side/studentsignup.html', {'user_data': user_data})



def studentlogin(request):
    return render(request,'student_side/studentlogin.html')


def addstudent(request):
    return render(request,'AddStudent/addstudent.html')
