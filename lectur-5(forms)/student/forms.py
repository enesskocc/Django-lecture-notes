from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Student


# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     number = forms.IntegerField(required=False)
#     profile_img = forms.ImageField(required=False)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (  # '__all__' asagidakinin kisa yolu.Bununla beraber database ki bütün verileri alir, asagidakini uzun uzun yazmaya gerek kalmaz.
            "first_name",
            "last_name",
            "number",
            "profile_pic"
        )
        labels = {"first_name" : "Name"}