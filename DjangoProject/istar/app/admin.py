from django.contrib import admin

# Register your models here.

# from .models import cr_student

# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ('E_name', )


# admin.site.register(cr_student)
# class cr_student(admin.ModelAdmin):
#     crname = ('crname',)
#     crpassword = ('crpassword',)
#     cremail = ('cremail',)


from .models import StudentUser

admin.site.register(StudentUser)


from  .models import StudentData
@admin.register(StudentData)
class StudentData(admin.ModelAdmin):
    list_display = ["id", "StudentName" ,"StudentEmail"]