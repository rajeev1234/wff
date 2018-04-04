
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Location_Amenitie_Amenitie : Location_Amenitie_list

    path('', views.Location_AmenitieListView.as_view(), name='Location_Amenitie_list'),

    # Path to create new Location_Amenitie : Location_Amenitie_new

    path('new/', views.Location_AmenitieCreateView.as_view(), name='Location_Amenitie_new'),

    # Path to edit Location_Amenitie : edit_list

    path('<int:pk>/edit', views.Location_AmenitieUpdateView.as_view(), name='Location_Amenitie_edit'),

    # Path to delete Location_Amenitie : Location_Amenitie_delete

    path('<int:pk>/delete', views.Location_AmenitieDeleteView.as_view(), name='Location_Amenitie_delete'),

    # Path to detail view of Location_Amenitie : Location_Amenitie_details

    path('<int:pk>', views.Location_AmenitieDetailView.as_view(), name='Location_Amenitie_details')
]
