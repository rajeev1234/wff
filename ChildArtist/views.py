# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create childartist Here

class ChildArtistCreateView(LoginRequiredMixin, CreateView):
    model = models.ChildArtist
    template_name = 'childartist/childartist_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['ChildArtist_Body_Type',
'ChildArtist_Child_Artist_Id',
'ChildArtist_Daily_Charges',
'ChildArtist_Description',
'ChildArtist_Ethnicity',
'ChildArtist_Eye_Color',
'ChildArtist_Financial_Available',
'ChildArtist_Gender',
'ChildArtist_Height',
'ChildArtist_Relation_With_Artist',
'ChildArtist_Skin_Color',
'ChildArtist_Special_Skills',
'ChildArtist_Weight']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# childartist Details Here


class ChildArtistDetailView(LoginRequiredMixin, DetailView):
    model = models.ChildArtist
    template_name = 'childartist/childartist_detail.html'
    login_url = 'login'

# childartist ListView Here


class ChildArtistListView(ListView):
    model = models.ChildArtist
    template_name = 'childartist/childartist_list.html'
    login_url = 'login'

# childartist Update Here


class ChildArtistUpdateView(LoginRequiredMixin, UpdateView):
    model = models.ChildArtist

    # Decide fields for editing Here

    fields = ['ChildArtist_Body_Type',
'ChildArtist_Child_Artist_Id',
'ChildArtist_Daily_Charges',
'ChildArtist_Description',
'ChildArtist_Ethnicity',
'ChildArtist_Eye_Color',
'ChildArtist_Financial_Available',
'ChildArtist_Gender',
'ChildArtist_Height',
'ChildArtist_Relation_With_Artist',
'ChildArtist_Skin_Color',
'ChildArtist_Special_Skills',
'ChildArtist_Weight']

    template_name = 'childartist/childartist_update.html'
    login_url = 'login'

# childartist Delete here


class ChildArtistDeleteView(LoginRequiredMixin, DeleteView):
    model = models.ChildArtist
    template_name = 'childartist/childartist_delete.html'
    success_url = reverse_lazy('childartist_list')
    login_url = 'login'



