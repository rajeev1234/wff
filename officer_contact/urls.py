
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of officer_contact : officer_contact_list

    path('', views.OfficerContactListView.as_view(), name='officer_contact_list'),

    # Path to create new officer_contact : officer_contact_new

    path('new/', views.OfficerContactCreateView.as_view(), name='officer_contact_new'),

    # Path to edit officer_contact : edit_list

    path('<int:pk>/edit', views.OfficerContactUpdateView.as_view(), name='officer_contact_edit'),

    # Path to delete officer_contact : officer_contact_delete

    path('<int:pk>/delete', views.OfficerContactDeleteView.as_view(), name='officer_contact_delete'),

    # Path to detail view of officer_contact : officer_contact_details

    path('<int:pk>', views.OfficerContactDetailView.as_view(), name='officer_contact_details')
]
