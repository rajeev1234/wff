from django.shortcuts import render

from django.urls import reverse_lazy

from django.views import generic

from .forms import CustomUserCreationForm


# Create your views here.

# creating signup view for user

class SignUp(generic.CreateView):

    form_class = CustomUserCreationForm

    success_url = reverse_lazy('login')

    template_name = 'signup.html'

def home(request):
    return render(request, 'home.html')
