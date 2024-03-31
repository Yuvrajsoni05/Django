from django.db import models


# Create your models here.

# class cr_student(models.Model):
#
#     crname = models.CharField(max_length=50)
#     crpassword = models.CharField(max_length=50)
#     cremail = models.EmailField(max_length=50)

class StudentUser(models.Model):
    cr_name = models.CharField(max_length=100)



class StudentData(models.Model):
    StudentName = models.CharField(max_length=100, verbose_name="Student Name")
    StudentEmail = models.EmailField(max_length=299,verbose_name="Student Email")


    def __str__(self):
        return str(self.id)

