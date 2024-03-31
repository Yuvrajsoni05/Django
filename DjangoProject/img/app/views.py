from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def IndexPage(request):
    return render(request,"app/index.html")




def UploadImage(request):
    if request.method == "POST":
        imagename = request.POST['imgname']
        pics = request.FILES['image']

        newimg = ImageData.objects.create(Imagename=imagename,Image=pics)
        return redirect('show')


def ImageFatch(request):
    all_img = ImageData.objects.all()
    return render(request,"app/show.html",{'key1':all_img})
