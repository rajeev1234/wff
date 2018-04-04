
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of profile_projects : profile_projects_list

    path('', views.profile_projectsListView.as_view(), name='profile_projects_list'),

    # Path to create new profile_projects : profile_projects_new

    path('new/', views.profile_projectsCreateView.as_view(), name='profile_projects_new'),

    # Path to edit profile_projects : edit_list

    path('<int:pk>/edit', views.profile_projectsUpdateView.as_view(), name='profile_projects_edit'),

    # Path to delete profile_projects : profile_projects_delete

    path('<int:pk>/delete', views.profile_projectsDeleteView.as_view(), name='profile_projects_delete'),

    # Path to detail view of profile_projects : profile_projects_details

    path('<int:pk>', views.profile_projectsDetailView.as_view(), name='profile_projects_details')
]
