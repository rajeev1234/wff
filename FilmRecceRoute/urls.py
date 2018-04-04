
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of FilmRecceRoute : FilmRecceRoute_list

    path('', views.FilmRecceRouteListView.as_view(), name='FilmRecceRoute_list'),

    # Path to create new FilmRecceRoute : FilmRecceRoute_new

    path('new/', views.FilmRecceRouteCreateView.as_view(), name='FilmRecceRoute_new'),

    # Path to edit FilmRecceRoute : edit_list

    path('<int:pk>/edit', views.FilmRecceRouteUpdateView.as_view(), name='FilmRecceRoute_update'),

    # Path to delete FilmRecceRoute : FilmRecceRoute_delete

    path('<int:pk>/delete', views.FilmRecceRouteDeleteView.as_view(), name='FilmRecceRoute_delete'),

    # Path to detail view of FilmRecceRoute : FilmRecceRoute_details

    path('<int:pk>', views.FilmRecceRouteDetailView.as_view(), name='FilmRecceRoute_details')
]
