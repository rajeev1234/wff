
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of District : District_list

    path('', views.DistrictListView.as_view(), name='District_list'),

    # Path to create new District : District_new

    path('new/', views.DistrictCreateView.as_view(), name='District_new'),

    # Path to edit District : edit_list

    path('<int:pk>/edit', views.DistrictUpdateView.as_view(), name='District_update'),

    # Path to delete District : District_delete

    path('<int:pk>/delete', views.DistrictDeleteView.as_view(), name='District_delete'),

    # Path to detail view of District : District_details

    path('<int:pk>', views.DistrictDetailView.as_view(), name='District_details')
]