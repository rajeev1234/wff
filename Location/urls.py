
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Location : Location_list

    path('', views.LocationListView.as_view(), name='Location_list'),

    # Path to create new Location : Location_new

    path('new/', views.LocationCreateView.as_view(), name='Location_new'),

    # Path to edit Location : edit_list

    path('<int:pk>/edit', views.LocationUpdateView.as_view(), name='Location_edit'),

    # Path to delete Location : Location_delete

    path('<int:pk>/delete', views.LocationDeleteView.as_view(), name='Location_delete'),

    # Path to detail view of Location : Location_details

    path('<int:pk>', views.LocationDetailView.as_view(), name='Location_details')
]
