
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of images : images_list

    path('', views.imagesListView.as_view(), name='images_list'),

    # Path to create new images : images_new

    path('new/', views.imagesCreateView.as_view(), name='images_new'),

    # Path to edit images : edit_list

    path('<int:pk>/edit', views.imagesUpdateView.as_view(), name='images_edit'),

    # Path to delete images : images_delete

    path('<int:pk>/delete', views.imagesDeleteView.as_view(), name='images_delete'),

    # Path to detail view of images : images_details

    path('<int:pk>', views.imagesDetailView.as_view(), name='images_details')
]
