
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of FilmLocationScheduleForPermit : FilmLocationScheduleForPermit_list

    path('', views.FilmLocationScheduleForPermitListView.as_view(), name='FilmLocationScheduleForPermit_list'),

    # Path to create new FilmLocationScheduleForPermit : FilmLocationScheduleForPermit_new

    path('new/', views.FilmLocationScheduleForPermitCreateView.as_view(), name='FilmLocationScheduleForPermit_new'),

    # Path to edit FilmLocationScheduleForPermit : edit_list

    path('<int:pk>/edit', views.FilmLocationScheduleForPermitUpdateView.as_view(), name='FilmLocationScheduleForPermit_update'),

    # Path to delete FilmLocationScheduleForPermit : FilmLocationScheduleForPermit_delete

    path('<int:pk>/delete', views.FilmLocationScheduleForPermitDeleteView.as_view(), name='FilmLocationScheduleForPermit_delete'),

    # Path to detail view of FilmLocationScheduleForPermit : FilmLocationScheduleForPermit_details

    path('<int:pk>', views.FilmLocationScheduleForPermitDetailView.as_view(), name='FilmLocationScheduleForPermit_details')
]
