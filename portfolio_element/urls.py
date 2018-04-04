
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of portfolio_element : portfolio_element_list

    path('', views.PortfolioElementListView.as_view(), name='portfolio_element_list'),

    # Path to create new portfolio_element : portfolio_element_new

    path('new/', views.PortfolioElementCreateView.as_view(), name='portfolio_element_new'),

    # Path to edit portfolio_element : edit_list

    path('<int:pk>/edit', views.PortfolioElementUpdateView.as_view(), name='portfolio_element_edit'),

    # Path to delete portfolio_element : portfolio_element_delete

    path('<int:pk>/delete', views.PortfolioElementDeleteView.as_view(), name='portfolio_element_delete'),

    # Path to detail view of portfolio_element : portfolio_element_details

    path('<int:pk>', views.PortfolioElementDetailView.as_view(), name='portfolio_element_details')
]
