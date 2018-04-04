# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Model Here

class ModelsCreateView(LoginRequiredMixin, CreateView):
    model = models.Models
    template_name = 'models/Model_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Models_Body_Type','Models_Description','Models_Ethnicity','Models_Eye_Colour','Models_Hair_Colour','Models_Height','Models_Scene_Comfort','Models_Skin_Color','Models_Smoker','Models_Special_Skills','Models_Weight']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Models_Author = self.request.user
        return super().form_valid(form)

# Model Details Here


class ModelsDetailView(LoginRequiredMixin, DetailView):
    model = models.Models
    context_object_name = 'Models'
    template_name = 'models/Model_detail.html'
    login_url = 'login'

# Model ListView Here


class ModelsListView(ListView):
    model = models.Models
    template_name = 'models/Model_list.html'
    login_url = 'login'

# Model Update Here


class ModelsUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Models

    # Decide fields for editing Here

    fields = ['Models_Body_Type','Models_Description','Models_Ethnicity','Models_Eye_Colour','Models_Hair_Colour','Models_Height','Models_Scene_Comfort','Models_Skin_Color','Models_Smoker','Models_Special_Skills','Models_Weight']
    template_name = 'models/Model_update.html'
    login_url = 'login'

# Model Delete here


class ModelsDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Models
    template_name = 'models/Model_delete.html'
    success_url = reverse_lazy('Model_list')
    login_url = 'login'
