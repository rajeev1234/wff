
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of conversations : conversations_list

    path('', views.ConversationsListView.as_view(), name='conversations_list'),

    # Path to create new conversations : conversations_new

    path('new/', views.ConversationsCreateView.as_view(), name='conversations_new'),

    # Path to edit conversations : edit_list

    path('<int:pk>/edit', views.ConversationsUpdateView.as_view(), name='conversations_edit'),

    # Path to delete conversations : conversations_delete

    path('<int:pk>/delete', views.ConversationsDeleteView.as_view(), name='conversations_delete'),

    # Path to detail view of conversations : conversations_details

    path('<int:pk>', views.ConversationsDetailView.as_view(), name='conversations_details')
]
