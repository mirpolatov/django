from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from apps.forms import RegisterForm, LoginForm


class RegisterView(View):

    def get(self, request):
        context = {
            'form': RegisterForm()
        }
        return render(request, 'register.html', context)

    def post(self, request):
        create_user = RegisterForm(data=request.POST)

        if create_user.is_valid():
            create_user.save()
            return render(request, 'login.html')
        else:
            context = {
                'form': create_user
            }
            return render(request, 'login.html', context)


def home(request):
    return render(request, 'home.html')


class LoginView(View):
    def get(self, request):
        context = {
            'form': LoginForm()
        }
        return render(request, 'login.html', context)

    def post(self, request):
        user = LoginForm(data=request.POST)
        if user.is_valid():
            return render(request, 'home.html')
        else:
            context = {
                'form': user,
                'errors': "ERROR"
            }
            return render(request, 'login.html', context)

# class MyUserRegisterTemplateView(TemplateView):
#     template_name = 'register.html'
#
#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         context['form'] = MyUserModelForm()
#         return context
