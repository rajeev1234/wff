# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create EducationInfo Here

class EducationInfoCreateView(LoginRequiredMixin, CreateView):
    model = models.EducationInfo
    template_name = 'EducationInfos/EducationInfo_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
            'EducationInfo_Course',
            'EducationInfo_Course_Detail',
            'EducationInfo_Institute',
            'EducationInfo_Passing_Year',
            'EducationInfo_Creator'
            ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.EducationInfo_Author = self.request.user
        return super().form_valid(form)

# EducationInfo Details Here


class EducationInfoDetailView(LoginRequiredMixin, DetailView):
    model = models.EducationInfo
    context_object_name = 'EducationInfo'
    template_name = 'EducationInfos/EducationInfo_details.html'
    login_url = 'login'

# EducationInfo ListView Here


class EducationInfoListView(ListView):
    model = models.EducationInfo
    template_name = 'EducationInfos/EducationInfo_list.html'
    login_url = 'login'

# EducationInfo Update Here


class EducationInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = models.EducationInfo

    # Decide fields for editing Here


    fields = [
            'EducationInfo_Course',
            'EducationInfo_Course_Detail',
            'EducationInfo_Institute',
            'EducationInfo_Passing_Year',
            'EducationInfo_Creator'
            ]
    template_name = 'EducationInfos/EducationInfo_update.html'
    login_url = 'login'

# EducationInfo Delete here


class EducationInfoDeleteView(LoginRequiredMixin, DeleteView):
    model = models.EducationInfo
    template_name = 'EducationInfos/EducationInfo_delete.html'
    success_url = reverse_lazy('EducationInfo_list')
    login_url = 'login'



