
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of SubscriptionPlan : SubscriptionPlan_list

    path('', views.SubscriptionPlanListView.as_view(), name='SubscriptionPlan_list'),

    # Path to create new SubscriptionPlan : SubscriptionPlan_new

    path('new/', views.SubscriptionPlanCreateView.as_view(), name='SubscriptionPlan_new'),

    # Path to edit SubscriptionPlan : edit_list

    path('<int:pk>/edit', views.SubscriptionPlanUpdateView.as_view(), name='SubscriptionPlan_update'),

    # Path to delete SubscriptionPlan : SubscriptionPlan_delete

    path('<int:pk>/delete', views.SubscriptionPlanDeleteView.as_view(), name='SubscriptionPlan_delete'),

    # Path to detail view of SubscriptionPlan : SubscriptionPlan_details

    path('<int:pk>', views.SubscriptionPlanDetailView.as_view(), name='SubscriptionPlan_details')
]
