
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of helpcenter : helpcenter_list

    path('', views.HelpCenterListView.as_view(), name='helpcenter_list'),

    # Path to create new helpcenter : helpcenter_new

    path('new/', views.HelpCenterCreateView.as_view(), name='helpcenter_new'),

    # Path to edit helpcenter : edit_list

    path('<int:pk>/edit', views.HelpCenterUpdateView.as_view(), name='helpcenter_edit'),

    # Path to delete helpcenter : helpcenter_delete

    path('<int:pk>/delete', views.HelpCenterDeleteView.as_view(), name='helpcenter_delete'),

    # Path to detail view of helpcenter : helpcenter_details

    path('<int:pk>', views.HelpCenterDetailView.as_view(), name='helpcenter_details')
]
