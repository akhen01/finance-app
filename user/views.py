from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

class CustomLogin(LoginView):
    template_name = "user/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("M-list")
    
class RegisterForm(FormView):
    template_name = "user/login.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("M-list")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterForm, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("M-list")
        return super(RegisterForm, self).get(*args, **kwargs)