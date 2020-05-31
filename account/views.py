from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request,'account/home.html')

# class Register(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'account/register.html'
def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()
	    return redirect("login")
    else:
	    form = RegisterForm()

    return render(response, "account/register.html", {"form":form})