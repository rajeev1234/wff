
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of messages : messages_list

    path('', views.MessagesListView.as_view(), name='messages_list'),

    # Path to create new messages : messages_new

    path('new/', views.MessagesCreateView.as_view(), name='messages_new'),

    # Path to edit messages : edit_list

    path('<int:pk>/edit', views.MessagesUpdateView.as_view(), name='messages_edit'),

    # Path to delete messages : messages_delete

    path('<int:pk>/delete', views.MessagesDeleteView.as_view(), name='messages_delete'),

    # Path to detail view of messages : messages_details

    path('<int:pk>', views.MessagesDetailView.as_view(), name='messages_details')
]
