
from django.urls import path

from . import views

# views.LocationFinancialListView.as_view()

urlpatterns = [

    # Path to list view of location_financial : location_financial_list

    path('', views.LocationFinancialListView.as_view(), name='location_financial_list'),

    # Path to create new location_financial : location_financial_new

    path('new/', views.LocationFinancialCreateView.as_view(), name='location_financial_new'),

    # Path to edit location_financial : edit_list

    path('<int:pk>/edit', views.LocationFinancialUpdateView.as_view(), name='location_financial_update'),

    # Path to delete location_financial : location_financial_delete

    path('<int:pk>/delete', views.LocationFinancialDeleteView.as_view(), name='location_financial_delete'),

    # Path to detail view of location_financial : location_financial_details

    path('<int:pk>', views.LocationFinancialDetailView.as_view(), name='location_financial_details')
]
