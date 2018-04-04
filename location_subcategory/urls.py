
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of location_subcategory : location_subcategory_list

    path('', views.LocationSubCategoryListView.as_view(), name='location_subcategory_list'),

    # Path to create new location_subcategory : location_subcategory_new

    path('new/', views.LocationSubCategoryCreateView.as_view(), name='location_subcategory_new'),

    # Path to edit location_subcategory : edit_list

    path('<int:pk>/edit', views.LocationSubCategoryUpdateView.as_view(), name='location_subcategory_edit'),

    # Path to delete location_subcategory : location_subcategory_delete

    path('<int:pk>/delete', views.LocationSubCategoryDeleteView.as_view(), name='location_subcategory_delete'),

    # Path to detail view of location_subcategory : location_subcategory_details

    path('<int:pk>', views.LocationSubCategoryDetailView.as_view(), name='location_subcategory_details')
]
