
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of amenity_adresses : amenity_adresses_list

    path('', views.AmenityAdressesListView.as_view(), name='amenity_adresses_list'),

    # Path to create new amenity_adresses : amenity_adresses_new

    path('new/', views.AmenityAdressesCreateView.as_view(), name='amenity_adresses_new'),

    # Path to edit amenity_adresses : edit_list

    path('<int:pk>/edit', views.AmenityAdressesUpdateView.as_view(), name='amenity_adresses_edit'),

    # Path to delete amenity_adresses : amenity_adresses_delete

    path('<int:pk>/delete', views.AmenityAdressesDeleteView.as_view(), name='amenity_adresses_delete'),

    # Path to detail view of amenity_adresses : amenity_adresses_details

    path('<int:pk>', views.AmenityAdressesDetailView.as_view(), name='amenity_adresses_details')
]
