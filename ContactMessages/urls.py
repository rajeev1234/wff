
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of contactmessages : contactmessages_list

    path('', views.ContactMessagesListView.as_view(), name='contactmessages_list'),

    # Path to create new contactmessages : contactmessages_new

    path('new/', views.ContactMessagesCreateView.as_view(), name='contactmessages_new'),

    # Path to edit contactmessages : edit_list

    path('<int:pk>/edit', views.ContactMessagesUpdateView.as_view(), name='contactmessages_edit'),

    # Path to delete contactmessages : contactmessages_delete

    path('<int:pk>/delete', views.ContactMessagesDeleteView.as_view(), name='contactmessages_delete'),

    # Path to detail view of contactmessages : contactmessages_details

    path('<int:pk>', views.ContactMessagesDetailView.as_view(), name='contactmessages_details')
]
