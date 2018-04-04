
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Actor : Actor_list

    path('', views.ActorListView.as_view(), name='actors_list'),

    # Path to create new Actor : Actor_new

    path('new/', views.ActorCreateView.as_view(), name='actors_new'),

    # Path to edit Actor : edit_list

    path('<int:pk>/edit', views.ActorUpdateView.as_view(), name='actors_edit'),

    # Path to delete Actor : Actor_delete

    path('<int:pk>/delete', views.ActorDeleteView.as_view(), name='actors_delete'),

    # Path to detail view of Actor : Actor_details

    path('<int:pk>', views.ActorDetailView.as_view(), name='actors_details')
]
