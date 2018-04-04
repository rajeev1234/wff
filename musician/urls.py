
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of musician : musician_list

    path('', views.MusicianListView.as_view(), name='musician_list'),

    # Path to create new musician : musician_new

    path('new/', views.MusicianCreateView.as_view(), name='musician_new'),

    # Path to edit musician : edit_list

    path('<int:pk>/edit', views.MusicianUpdateView.as_view(), name='musician_edit'),

    # Path to delete musician : musician_delete

    path('<int:pk>/delete', views.MusicianDeleteView.as_view(), name='musician_delete'),

    # Path to detail view of musician : musician_details

    path('<int:pk>', views.MusicianDetailView.as_view(), name='musician_details')
]
