from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email') ## hepsi icin '__all__'


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # fields = ('portfolio', 'profile_pic') ## asagidaki daha kisa yol.
        exclude = ('user',) ## burda diyoruz ki, user field kullanma, digerlerini kullan.