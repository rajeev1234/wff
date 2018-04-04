
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of subcription_plan : subcription_plan_list

    path('', views.subcription_planListView.as_view(), name='subcription_plan_list'),

    # Path to create new subcription_plan : subcription_plan_new

    path('new/', views.subcription_planCreateView.as_view(), name='subcription_plan_new'),

    # Path to edit subcription_plan : edit_list

    path('<int:pk>/edit', views.subcription_planUpdateView.as_view(), name='subcription_plan_edit'),

    # Path to delete subcription_plan : subcription_plan_delete

    path('<int:pk>/delete', views.subcription_planDeleteView.as_view(), name='subcription_plan_delete'),

    # Path to detail view of subcription_plan : subcription_plan_details

    path('<int:pk>', views.subcription_planDetailView.as_view(), name='subcription_plan_details')
]
