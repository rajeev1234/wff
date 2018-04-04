
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of userprofessionalinfo : userprofessionalinfo_list

    path('', views.UserProfessionalInfoListView.as_view(), name='userprofessionalinfo_list'),

    # Path to create new userprofessionalinfo : userprofessionalinfo_new

    path('new/', views.UserProfessionalInfoCreateView.as_view(), name='userprofessionalinfo_new'),

    # Path to edit userprofessionalinfo : edit_list

    path('<int:pk>/edit', views.UserProfessionalInfoUpdateView.as_view(), name='userprofessionalinfo_edit'),

    # Path to delete userprofessionalinfo : userprofessionalinfo_delete

    path('<int:pk>/delete', views.UserProfessionalInfoDeleteView.as_view(), name='userprofessionalinfo_delete'),

    # Path to detail view of userprofessionalinfo : userprofessionalinfo_details

    path('<int:pk>', views.UserProfessionalInfoDetailView.as_view(), name='userprofessionalinfo_details')
]
