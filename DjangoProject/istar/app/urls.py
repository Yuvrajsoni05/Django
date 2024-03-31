from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('app.urls'))
    path('',views.home,name='home'),
    path('adminLogin',views.adminLogin,name='adminLogin'),
    path('adminSignup',views.adminSignup,name='adminSignup'),
    path('adminHome',views.adminHome,name='adminHome'),
    path('adminLogout',views.adminLogout,name='adminLogout'),
    path('studentsignup',views.studentsignup,name='studentsignup'),
    path('studentlogin',views.studentlogin,name='studentlogin'),
    path('addstudent',views.addstudent,name='addstudent'),



]

