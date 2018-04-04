
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of platform_works : platform_works_list

    path('', views.PlatformWorksListView.as_view(), name='platform_works_list'),

    # Path to create new platform_works : platform_works_new

    path('new/', views.PlatformWorksCreateView.as_view(), name='platform_works_new'),

    # Path to edit platform_works : edit_list

    path('<int:pk>/edit', views.PlatformWorksUpdateView.as_view(), name='platform_works_edit'),

    # Path to delete platform_works : platform_works_delete

    path('<int:pk>/delete', views.PlatformWorksDeleteView.as_view(), name='platform_works_delete'),

    # Path to detail view of platform_works : platform_works_details

    path('<int:pk>', views.PlatformWorksDetailView.as_view(), name='platform_works_details')
]
