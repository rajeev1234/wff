
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of voiceoverartist : voiceoverartist_list

    path('', views.VoiceOverArtistListView.as_view(), name='voiceoverartist_list'),

    # Path to create new voiceoverartist : voiceoverartist_new

    path('new/', views.VoiceOverArtistCreateView.as_view(), name='voiceoverartist_new'),

    # Path to edit voiceoverartist : edit_list

    path('<int:pk>/edit', views.VoiceOverArtistUpdateView.as_view(), name='voiceoverartist_edit'),

    # Path to delete voiceoverartist : voiceoverartist_delete

    path('<int:pk>/delete', views.VoiceOverArtistDeleteView.as_view(), name='voiceoverartist_delete'),

    # Path to detail view of voiceoverartist : voiceoverartist_details

    path('<int:pk>', views.VoiceOverArtistDetailView.as_view(), name='voiceoverartist_details')
]
