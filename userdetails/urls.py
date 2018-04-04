
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of userdetails : userdetails_list

    path('', views.UserDetailsListView.as_view(), name='userdetails_list'),

    # Path to create new userdetails : userdetails_new

    path('new/', views.UserDetailsCreateView.as_view(), name='userdetails_new'),

    # Path to edit userdetails : edit_list

    path('<int:pk>/edit', views.UserDetailsUpdateView.as_view(), name='userdetails_edit'),

    # Path to delete userdetails : userdetails_delete

    path('<int:pk>/delete', views.UserDetailsDeleteView.as_view(), name='userdetails_delete'),

    # Path to detail view of userdetails : userdetails_details

    path('<int:pk>', views.UserDetailsDetailView.as_view(), name='userdetails_details')
]
