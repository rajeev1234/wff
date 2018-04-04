
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of location_psndc : location_psndc_list

    path('', views.LocationPSnDCListView.as_view(), name='location_psndc_list'),

    # Path to create new location_psndc : location_psndc_new

    path('new/', views.LocationPSnDCCreateView.as_view(), name='location_psndc_new'),

    # Path to edit location_psndc : edit_list

    path('<int:pk>/edit', views.LocationPSnDCUpdateView.as_view(), name='location_psndc_update'),

    # Path to delete location_psndc : location_psndc_delete

    path('<int:pk>/delete', views.LocationPSnDCDeleteView.as_view(), name='location_psndc_delete'),

    # Path to detail view of location_psndc : location_psndc_details

    path('<int:pk>', views.LocationPSnDCDetailView.as_view(), name='location_psndc_details')
]
