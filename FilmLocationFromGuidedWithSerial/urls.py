
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of FilmLocationFromGuidedWithSerial : FilmLocationFromGuidedWithSerial_list

    path('', views.FilmLocationFromGuidedWithSerialListView.as_view(), name='FilmLocationFromGuidedWithSerial_list'),

    # Path to create new FilmLocationFromGuidedWithSerial : FilmLocationFromGuidedWithSerial_new

    path('new/', views.FilmLocationFromGuidedWithSerialCreateView.as_view(), name='FilmLocationFromGuidedWithSerial_new'),

    # Path to edit FilmLocationFromGuidedWithSerial : edit_list

    path('<int:pk>/edit', views.FilmLocationFromGuidedWithSerialUpdateView.as_view(), name='FilmLocationFromGuidedWithSerial_update'),

    # Path to delete FilmLocationFromGuidedWithSerial : FilmLocationFromGuidedWithSerial_delete

    path('<int:pk>/delete', views.FilmLocationFromGuidedWithSerialDeleteView.as_view(), name='FilmLocationFromGuidedWithSerial_delete'),

    # Path to detail view of FilmLocationFromGuidedWithSerial : FilmLocationFromGuidedWithSerial_details

    path('<int:pk>', views.FilmLocationFromGuidedWithSerialDetailView.as_view(), name='FilmLocationFromGuidedWithSerial_details')
]
