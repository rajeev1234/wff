
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Rating_Amenitie : Rating_list

    path('', views.RatingListView.as_view(), name='Rating_list'),

    # Path to create new Rating : Rating_new

    path('new/', views.RatingCreateView.as_view(), name='Rating_new'),

    # Path to edit Rating : edit_list

    path('<int:pk>/edit', views.RatingUpdateView.as_view(), name='Rating_edit'),

    # Path to delete Rating : Rating_delete

    path('<int:pk>/delete', views.RatingDeleteView.as_view(), name='Rating_delete'),

    # Path to detail view of Rating : Rating_details

    path('<int:pk>', views.RatingDetailView.as_view(), name='Rating_details')
]
