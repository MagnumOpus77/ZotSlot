from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=8, default="", unique=False)

    def __str__(self):
        return self.name




class CourseCode(models.Model):
    username = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    code = models.CharField(max_length=5, default="", unique=False)

    class_abr = models.CharField(max_length=100, default="")
    class_name = models.CharField(max_length=100, default="")
    instructors = models.CharField(max_length=100, default="")
    class_time = models.CharField(max_length=100, default="")
    class_type = models.CharField(max_length=100, default="")
    units = models.CharField(max_length=100, default="")
    max_capacity = models.CharField(max_length=100, default="")
    enrolled = models.CharField(max_length=100, default="")
    waitlisted = models.CharField(max_length=100, default="")
    requested = models.CharField(max_length=100, default="")
    reserved_new = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return self.code

