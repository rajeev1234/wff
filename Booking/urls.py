
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of booking : booking_list

    path('', views.BookingListView.as_view(), name='booking_list'),

    # Path to create new booking : booking_new

    path('new/', views.BookingCreateView.as_view(), name='booking_new'),

    # Path to edit booking : edit_list

    path('<int:pk>/edit', views.BookingUpdateView.as_view(), name='booking_edit'),

    # Path to delete booking : booking_delete

    path('<int:pk>/delete', views.BookingDeleteView.as_view(), name='booking_delete'),

    # Path to detail view of booking : booking_details

    path('<int:pk>', views.BookingDetailView.as_view(), name='booking_details')
]
