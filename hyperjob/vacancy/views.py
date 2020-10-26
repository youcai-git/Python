from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Vacancy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu/menu.html')


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/vacancy.html', context={"vacancies": Vacancy.objects.all()})


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "signup/signup.html"


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "login/login.html"
