
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of SpecialArt : SpecialArt_list

    path('', views.SpecialArtListView.as_view(), name='SpecialArt_list'),

    # Path to create new SpecialArt : SpecialArt_new

    path('new/', views.SpecialArtCreateView.as_view(), name='SpecialArt_new'),

    # Path to edit SpecialArt : edit_list

    path('<int:pk>/edit', views.SpecialArtUpdateView.as_view(), name='SpecialArt_update'),

    # Path to delete SpecialArt : SpecialArt_delete

    path('<int:pk>/delete', views.SpecialArtDeleteView.as_view(), name='SpecialArt_delete'),

    # Path to detail view of SpecialArt : SpecialArt_details

    path('<int:pk>', views.SpecialArtDetailView.as_view(), name='SpecialArt_details')
]
