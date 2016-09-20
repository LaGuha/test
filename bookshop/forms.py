from django import forms
from django.contrib.auth.models import User

class PostForm(forms.Form):
	username=forms.CharField(label="Логин", max_length=30, required=True)
	password=forms.CharField(label="Пароль", required=True)
   # class Meta:
    #    model = User
     #   fields = ('username', 'password',)