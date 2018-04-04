
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of pets : pets_list

    path('', views.PetsListView.as_view(), name='pets_list'),

    # Path to create new pets : pets_new

    path('new/', views.PetsCreateView.as_view(), name='pets_new'),

    # Path to edit pets : edit_list

    path('<int:pk>/edit', views.PetsUpdateView.as_view(), name='pets_edit'),

    # Path to delete pets : pets_delete

    path('<int:pk>/delete', views.PetsDeleteView.as_view(), name='pets_delete'),

    # Path to detail view of pets : pets_details

    path('<int:pk>', views.PetsDetailView.as_view(), name='pets_details')
]
