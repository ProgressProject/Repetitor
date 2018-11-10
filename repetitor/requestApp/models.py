from django.db import models
#test test
# from django.contrib.auth import get_user_model

# User = get_user_model()
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Course(models.Model):
    course_name = models.CharField('course_name', max_length = 150)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    courses = models.ForeignKey(Course, verbose_name="Course",
                                on_delete=models.CASCADE)
    name = models.CharField('name', max_length=150)
    last_name = models.CharField('last_name', max_length=150)
    phone = models.CharField('phone', max_length=12)
    date_pub = models.DateTimeField('date_pub', auto_now_add=True)
    email = models.EmailField('email')

    def __str__(self):
        return 'Имя {} Фамилия {}'.format(self.name, self.last_name)
