# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create helpQna Here

class helpQnaCreateView(LoginRequiredMixin, CreateView):
    model = models.HelpQna
    template_name = 'helpQna/helpQna_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Help_Qna_Answer','Help_Qna_Article_Id','Help_Qna_Question','Help_Qna_Creator']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.helpQna_Author = self.request.user
        return super().form_valid(form)

# helpQna Details Here


class helpQnaDetailView(LoginRequiredMixin, DetailView):
    model = models.HelpQna
    template_name = 'helpQna/helpQna_detail.html'
    login_url = 'login'

# helpQna ListView Here


class helpQnaListView(ListView):
    model = models.HelpQna
    template_name = 'helpQna/helpQna_list.html'
    login_url = 'login'

# helpQna Update Here


class helpQnaUpdateView(LoginRequiredMixin, UpdateView):
    model = models.HelpQna

    # Decide fields for editing Here

    fields = ['Help_Qna_Answer','Help_Qna_Article_Id','Help_Qna_Question','Help_Qna_Creator']
    template_name = 'helpQna/helpQna_update.html'
    login_url = 'login'

# helpQna Delete here


class helpQnaDeleteView(LoginRequiredMixin, DeleteView):
    model = models.HelpQna
    template_name = 'helpQna/helpQna_delete.html'
    success_url = reverse_lazy('helpQna_list')
    login_url = 'login'



