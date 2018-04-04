
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of police_station : police_station_list

    path('', views.PoliceStationListView.as_view(), name='police_station_list'),

    # Path to create new police_station : police_station_new

    path('new/', views.PoliceStationCreateView.as_view(), name='police_station_new'),

    # Path to edit police_station : edit_list

    path('<int:pk>/edit', views.PoliceStationUpdateView.as_view(), name='police_station_edit'),

    # Path to delete police_station : police_station_delete

    path('<int:pk>/delete', views.PoliceStationDeleteView.as_view(), name='police_station_delete'),

    # Path to detail view of police_station : police_station_details

    path('<int:pk>', views.PoliceStationDetailView.as_view(), name='police_station_details')
]
