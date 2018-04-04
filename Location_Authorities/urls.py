
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Location_Authoritis : Location_Authoritis_list

    path('', views.Location_AuthoritisListView.as_view(), name='Location_Authorities_list'),

    # Path to create new Location_Authoritis : Location_Authoritis_new

    path('new/', views.Location_AuthoritisCreateView.as_view(), name='Location_Authorities_new'),

    # Path to edit Location_Authoritis : edit_list

    path('<int:pk>/edit', views.Location_AuthoritisUpdateView.as_view(), name='Location_Authorities_edit'),

    # Path to delete Location_Authoritis : Location_Authoritis_delete

    path('<int:pk>/delete', views.Location_AuthoritisDeleteView.as_view(), name='Location_Authorities_delete'),

    # Path to detail view of Location_Authoritis : Location_Authoritis_details

    path('<int:pk>', views.Location_AuthoritisDetailView.as_view(), name='Location_Authorities_details')
]
