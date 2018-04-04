
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Singer : Singer_list

    path('', views.SingerListView.as_view(), name='Singer_list'),

    # Path to create new Singer : Singer_new

    path('new/', views.SingerCreateView.as_view(), name='Singer_new'),

    # Path to edit Singer : edit_list

    path('<int:pk>/edit', views.SingerUpdateView.as_view(), name='Singer_update'),

    # Path to delete Singer : Singer_delete

    path('<int:pk>/delete', views.SingerDeleteView.as_view(), name='Singer_delete'),

    # Path to detail view of Singer : Singer_details

    path('<int:pk>', views.SingerDetailView.as_view(), name='Singer_details')
]
