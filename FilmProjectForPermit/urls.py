
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of FilmProjectForPermit : FilmProjectForPermit_list

    path('', views.FilmProjectForPermitListView.as_view(), name='FilmProjectForPermit_list'),

    # Path to create new FilmProjectForPermit : FilmProjectForPermit_new

    path('new/', views.FilmProjectForPermitCreateView.as_view(), name='FilmProjectForPermit_new'),

    # Path to edit FilmProjectForPermit : edit_list

    path('<int:pk>/edit', views.FilmProjectForPermitUpdateView.as_view(), name='FilmProjectForPermit_update'),

    # Path to delete FilmProjectForPermit : FilmProjectForPermit_delete

    path('<int:pk>/delete', views.FilmProjectForPermitDeleteView.as_view(), name='FilmProjectForPermit_delete'),

    # Path to detail view of FilmProjectForPermit : FilmProjectForPermit_details

    path('<int:pk>', views.FilmProjectForPermitDetailView.as_view(), name='FilmProjectForPermit_details')
]
