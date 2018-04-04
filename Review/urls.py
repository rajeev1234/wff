
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Review_Amenitie : Review_list

    path('', views.ReviewListView.as_view(), name='Review_list'),

    # Path to create new Review : Review_new

    path('new/', views.ReviewCreateView.as_view(), name='Review_new'),

    # Path to edit Review : edit_list

    path('<int:pk>/edit', views.ReviewUpdateView.as_view(), name='Review_edit'),

    # Path to delete Review : Review_delete

    path('<int:pk>/delete', views.ReviewDeleteView.as_view(), name='Review_delete'),

    # Path to detail view of Review : Review_details

    path('<int:pk>', views.ReviewDetailView.as_view(), name='Review_details')
]
