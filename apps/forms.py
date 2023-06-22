from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=250)
    email = forms.EmailField()
    password = forms.CharField(max_length=250)

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = User.objects.create(
            username=username,
            email=email,
            password=password
        )
        # user.set_password(password)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)

    def is_valid(self):
        username = self.data.get('username')

        if User.objects.filter(username=username):
            return super().is_valid()
        else:
            return self.errors

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=250)
#     password = forms.CharField(max_length=250)
#
#     def is_valid(self):
#         username = self.data.get('username')
#
#
#         if User.objects.filter(username=username):
#                     return super().is_valid()
#                 else:
#                     return self.errors
#
#
