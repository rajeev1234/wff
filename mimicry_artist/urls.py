
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of mimicry_artist : mimicry_artist_list

    path('', views.MimicryArtistListView.as_view(), name='mimicry_artist_list'),

    # Path to create new mimicry_artist : mimicry_artist_new

    path('new/', views.MimicryArtistCreateView.as_view(), name='mimicry_artist_new'),

    # Path to edit mimicry_artist : edit_list

    path('<int:pk>/edit', views.MimicryArtistUpdateView.as_view(), name='mimicry_artist_edit'),

    # Path to delete mimicry_artist : mimicry_artist_delete

    path('<int:pk>/delete', views.MimicryArtistDeleteView.as_view(), name='mimicry_artist_delete'),

    # Path to detail view of mimicry_artist : mimicry_artist_details

    path('<int:pk>', views.MimicryArtistDetailView.as_view(), name='mimicry_artist_details')
]
