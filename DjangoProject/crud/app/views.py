from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def InsertPageView(request):
    return render(request,"app/insert.html")

def InsertData(request):

    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    #object
    newuser = Student.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,)


    return redirect('showpage')



def ShowPage(request):
    all_data = Student.objects.all()
    return render(request,"app/show.html",{'key1':all_data})


def EditPage(request,pk):
    get_data = Student.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})


def UpdateData(request,pk):
    updata = Student.objects.get(id=pk)
    updata.Firstname = request.POST['fname']
    updata.Lastname  = request.POST['lname']
    updata.Email = request.POST['email']
    updata.Contact = request.POST['contact']

    updata.save()
    return redirect('showpage')

def DeleteData(request,pk):
    ddata = Student.objects.get(id=pk)
    ddata.delete()
    return redirect('showpage')
