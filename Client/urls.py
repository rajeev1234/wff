
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of client : client_list

    path('', views.ClientListView.as_view(), name='client_list'),

    # Path to create new client : client_new

    path('new/', views.ClientCreateView.as_view(), name='client_new'),

    # Path to edit client : edit_list

    path('<int:pk>/edit', views.ClientUpdateView.as_view(), name='client_edit'),

    # Path to delete client : client_delete

    path('<int:pk>/delete', views.ClientDeleteView.as_view(), name='client_delete'),

    # Path to detail view of client : client_details

    path('<int:pk>', views.ClientDetailView.as_view(), name='client_details')
]
