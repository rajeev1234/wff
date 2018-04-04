
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Location_Category_Amenitie : Location_Category_list

    path('', views.Location_CategoryListView.as_view(), name='Location_Category_list'),

    # Path to create new Location_Category : Location_Category_new

    path('new/', views.Location_CategoryCreateView.as_view(), name='Location_Category_new'),

    # Path to edit Location_Category : edit_list

    path('<int:pk>/edit', views.Location_CategoryUpdateView.as_view(), name='Location_Category_edit'),

    # Path to delete Location_Category : Location_Category_delete

    path('<int:pk>/delete', views.Location_CategoryDeleteView.as_view(), name='Location_Category_delete'),

    # Path to detail view of Location_Category : Location_Category_details

    path('<int:pk>', views.Location_CategoryDetailView.as_view(), name='Location_Category_details')
]
