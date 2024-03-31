from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("upload",views.UploadImage,name="imageupload"),
    path('showing',views.ImageFatch,name="show")

]