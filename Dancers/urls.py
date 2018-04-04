
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Dancer : Dancer_list

    path('', views.DancerListView.as_view(), name='Dancer_list'),

    # Path to create new Dancer : Dancer_new

    path('new/', views.DancerCreateView.as_view(), name='Dancer_new'),

    # Path to edit Dancer : edit_list

    path('<int:pk>/edit', views.DancerUpdateView.as_view(), name='Dancer_update'),

    # Path to delete Dancer : Dancer_delete

    path('<int:pk>/delete', views.DancerDeleteView.as_view(), name='Dancer_delete'),

    # Path to detail view of Dancer : Dancer_details

    path('<int:pk>', views.DancerDetailView.as_view(), name='Dancer_details')
]
