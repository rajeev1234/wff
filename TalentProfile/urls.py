
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of TalentProfile : TalentProfile_list

    path('', views.TalentProfileListView.as_view(), name='TalentProfile_list'),

    # Path to create new TalentProfile : TalentProfile_new

    path('new/', views.TalentProfileCreateView.as_view(), name='TalentProfile_new'),

    # Path to edit TalentProfile : edit_list

    path('<int:pk>/edit', views.TalentProfileUpdateView.as_view(), name='TalentProfile_update'),

    # Path to delete TalentProfile : TalentProfile_delete

    path('<int:pk>/delete', views.TalentProfileDeleteView.as_view(), name='TalentProfile_delete'),

    # Path to detail view of TalentProfile : TalentProfile_details

    path('<int:pk>', views.TalentProfileDetailView.as_view(), name='TalentProfile_details')
]
