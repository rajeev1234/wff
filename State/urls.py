
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of State : State_list

    path('', views.StateListView.as_view(), name='State_list'),

    # Path to create new State : State_new

    path('new/', views.StateCreateView.as_view(), name='State_new'),

    # Path to edit State : edit_list

    path('<int:pk>/edit', views.StateUpdateView.as_view(), name='State_update'),

    # Path to delete State : State_delete

    path('<int:pk>/delete', views.StateDeleteView.as_view(), name='State_delete'),

    # Path to detail view of State : State_details

    path('<int:pk>', views.StateDetailView.as_view(), name='State_details')
]
