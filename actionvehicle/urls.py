
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of actionvehicle : actionvehicle_list

    path('', views.ActionVehicleListView.as_view(), name='actionvehicle_list'),

    # Path to create new actionvehicle : actionvehicle_new

    path('new/', views.ActionVehicleCreateView.as_view(), name='actionvehicle_new'),

    # Path to edit actionvehicle : edit_list

    path('<int:pk>/edit', views.ActionVehicleUpdateView.as_view(), name='actionvehicle_edit'),

    # Path to delete actionvehicle : actionvehicle_delete

    path('<int:pk>/delete', views.ActionVehicleDeleteView.as_view(), name='actionvehicle_delete'),

    # Path to detail view of actionvehicle : actionvehicle_details

    path('<int:pk>', views.ActionVehicleDetailView.as_view(), name='actionvehicle_details')
]
