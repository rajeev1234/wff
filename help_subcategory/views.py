# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create helpsubcategory Here

class helpsubcategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.HelpSubCategory
    template_name = 'helpsubcategory/helpsubcategory_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Help_SubCategory_Name','Help_SubCategory_Topic_Id','Help_SubCategory_Creator']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.helpsubcategory_Author = self.request.user
        return super().form_valid(form)

# helpsubcategory Details Here


class helpsubcategoryDetailView(LoginRequiredMixin, DetailView):
    model = models.HelpSubCategory
    template_name = 'helpsubcategory/helpsubcategory_detail.html'
    login_url = 'login'

# helpsubcategory ListView Here


class helpsubcategoryListView(ListView):
    model = models.HelpSubCategory
    template_name = 'helpsubcategory/helpsubcategory_list.html'
    login_url = 'login'

# helpsubcategory Update Here


class helpsubcategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.HelpSubCategory

    # Decide fields for editing Here

    fields = ['Help_SubCategory_Name','Help_SubCategory_Topic_Id','Help_SubCategory_Creator']
    template_name = 'helpsubcategory/helpsubcategory_update.html'
    login_url = 'login'

# helpsubcategory Delete here


class helpsubcategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.HelpSubCategory
    template_name = 'helpsubcategory/helpsubcategory_delete.html'
    success_url = reverse_lazy('helpsubcategory_list')
    login_url = 'login'



