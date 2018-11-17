# from .models import Student
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=30, label="name")
    surname = forms.CharField(max_length=30, label="Surname")
    senya = forms.CharField(max_length=30)

    def clean_senya(self):
        senya = self.cleaned_data["senya"]

        if senya == "Sen":
            raise forms.ValidationError("Ti ne prav")
        return senya
