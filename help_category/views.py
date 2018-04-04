# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create helpcategory Here

class Help_CategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.Help_Category
    template_name = 'helpcategorys/helpcategory_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Help_Category_Name','Help_Category_Header_Id','Help_Category_Creator',]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.helpcategory_Author = self.request.user
        return super().form_valid(form)


# helpcategory Details Here


class Help_CategoryDetailView(LoginRequiredMixin, DetailView):
    model = models.Help_Category
    template_name = 'helpcategorys/helpcategory_detail.html'
    login_url = 'login'

# helpcategory ListView Here


class Help_CategoryListView(ListView):
    model = models.Help_Category
    template_name = 'helpcategorys/helpcategory_list.html'
    login_url = 'login'

# helpcategory Update Here


class Help_CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Help_Category

    # Decide fields for editing Here

    fields = ['Help_Category_Name','Help_Category_Header_Id','Help_Category_Creator',]
    template_name = 'helpcategorys/helpcategory_update.html'
    login_url = 'login'

# helpcategory Delete here


class Help_CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Help_Category
    template_name = 'helpcategorys/helpcategory_delete.html'
    success_url = reverse_lazy('helpcategory_list')
    login_url = 'login'



