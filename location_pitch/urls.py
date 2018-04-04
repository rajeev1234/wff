
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of location_pitch : location_pitch_list

    path('', views.LocationPitchListView.as_view(), name='location_pitch_list'),

    # Path to create new location_pitch : location_pitch_new

    path('new/', views.LocationPitchCreateView.as_view(), name='location_pitch_new'),

    # Path to edit location_pitch : edit_list

    path('<int:pk>/edit', views.LocationPitchUpdateView.as_view(), name='location_pitch_edit'),

    # Path to delete location_pitch : location_pitch_delete

    path('<int:pk>/delete', views.LocationPitchDeleteView.as_view(), name='location_pitch_delete'),

    # Path to detail view of location_pitch : location_pitch_details

    path('<int:pk>', views.LocationPitchDetailView.as_view(), name='location_pitch_details')
]
