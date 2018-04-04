# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create UserCoinBox Here

class UserCoinBoxCreateView(LoginRequiredMixin, CreateView):
    model = models.UserCoinBox
    template_name = 'UserCoinBox/UserCoinBox_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
            'UserCoinBox_Costume_List',
            'UserCoinBox_Location_List',
            'UserCoinBox_Pet_List',
            'UserCoinBox_Prop_List',
            'UserCoinBox_Vehicle_List',
          ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        # form.instance.UserCoinBox_Author = self.request.user
        return super().form_valid(form)

# UserCoinBox Details Here


class UserCoinBoxDetailView(LoginRequiredMixin, DetailView):
    model = models.UserCoinBox
    context_object_name = 'UserCoinBox'
    template_name = 'UserCoinBox/UserCoinBox_details.html'
    login_url = 'login'

# UserCoinBox ListView Here


class UserCoinBoxListView(ListView):
    model = models.UserCoinBox
    template_name = 'UserCoinBox/UserCoinBox_list.html'
    login_url = 'login'

# UserCoinBox Update Here


class UserCoinBoxUpdateView(LoginRequiredMixin, UpdateView):
    model = models.UserCoinBox

    # Decide fields for editing Here

    fields = [
            'UserCoinBox_Costume_List',
            'UserCoinBox_Location_List',
            'UserCoinBox_Pet_List',
            'UserCoinBox_Prop_List',
            'UserCoinBox_Vehicle_List',
          ]


    template_name = 'UserCoinBox/UserCoinBox_update.html'
    login_url = 'login'

# UserCoinBox Delete here


class UserCoinBoxDeleteView(LoginRequiredMixin, DeleteView):
    model = models.UserCoinBox
    template_name = 'UserCoinBox/UserCoinBox_delete.html'
    success_url = reverse_lazy('UserCoinBox_list')
    login_url = 'login'