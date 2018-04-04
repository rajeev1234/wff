
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of circleinvite : circleinvite_list

    path('', views.CircleInviteListView.as_view(), name='circleinvite_list'),

    # Path to create new circleinvite : circleinvite_new

    path('new/', views.CircleInviteCreateView.as_view(), name='circleinvite_new'),

    # Path to edit circleinvite : edit_list

    path('<int:pk>/edit', views.CircleInviteUpdateView.as_view(), name='circleinvite_edit'),

    # Path to delete circleinvite : circleinvite_delete

    path('<int:pk>/delete', views.CircleInviteDeleteView.as_view(), name='circleinvite_delete'),

    # Path to detail view of circleinvite : circleinvite_details

    path('<int:pk>', views.CircleInviteDetailView.as_view(), name='circleinvite_details')
]
