from django import forms
from .models import Student



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['courses', 'name', 'last_name', 'phone', 'email']
    # name = forms.CharField(max_length=50)
    # last_name = forms.CharField(max_length=50)
    # phone = forms.CharField(max_length=30)
    # email = forms.EmailField(max_length=50)

    def save(self):
        new_student = Student.objects.create(
            courses = self.cleaned_data['courses'],
            name = self.cleaned_data['name'],
            last_name = self.cleaned_data['last_name'],
            phone = self.cleaned_data['phone'],
            email = self.cleaned_data['email'],
        )
