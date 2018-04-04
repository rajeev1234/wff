
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of FilmRecceTourGuide : FilmRecceTourGuide_list

    path('', views.FilmRecceTourGuideListView.as_view(), name='FilmRecceTourGuide_list'),

    # Path to create new FilmRecceTourGuide : FilmRecceTourGuide_new

    path('new/', views.FilmRecceTourGuideCreateView.as_view(), name='FilmRecceTourGuide_new'),

    # Path to edit FilmRecceTourGuide : edit_list

    path('<int:pk>/edit', views.FilmRecceTourGuideUpdateView.as_view(), name='FilmRecceTourGuide_update'),

    # Path to delete FilmRecceTourGuide : FilmRecceTourGuide_delete

    path('<int:pk>/delete', views.FilmRecceTourGuideDeleteView.as_view(), name='FilmRecceTourGuide_delete'),

    # Path to detail view of FilmRecceTourGuide : FilmRecceTourGuide_details

    path('<int:pk>', views.FilmRecceTourGuideDetailView.as_view(), name='FilmRecceTourGuide_details')
]
