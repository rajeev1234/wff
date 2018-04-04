
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of childartist : childartist_list

    path('', views.ChildArtistListView.as_view(), name='childartist_list'),

    # Path to create new childartist : childartist_new

    path('new/', views.ChildArtistCreateView.as_view(), name='childartist_new'),

    # Path to edit childartist : edit_list

    path('<int:pk>/edit', views.ChildArtistUpdateView.as_view(), name='childartist_edit'),

    # Path to delete childartist : childartist_delete

    path('<int:pk>/delete', views.ChildArtistDeleteView.as_view(), name='childartist_delete'),

    # Path to detail view of childartist : childartist_details

    path('<int:pk>', views.ChildArtistDetailView.as_view(), name='childartist_details')
]
