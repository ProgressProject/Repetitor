from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length = 150)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    courses = models.ForeignKey(Course, on_delete="CASCADE")
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    # phone = models.PhoneNumberField(null=False, blank=False, unique=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
