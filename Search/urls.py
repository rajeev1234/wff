
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of search_Amenitie : search_list

    path('', views.searchListView.as_view(), name='search_list'),

    # Path to create new search : search_new

    path('new/', views.searchCreateView.as_view(), name='search_new'),

    # Path to edit search : edit_list

    path('<int:pk>/edit', views.searchUpdateView.as_view(), name='search_edit'),

    # Path to delete search : search_delete

    path('<int:pk>/delete', views.searchDeleteView.as_view(), name='search_delete'),

    # Path to detail view of search : search_details

    path('<int:pk>', views.searchDetailView.as_view(), name='search_details')
]
