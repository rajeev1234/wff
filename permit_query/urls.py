
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of permit_query : permit_query_list

    path('', views.PermitQueryListView.as_view(), name='permit_query_list'),

    # Path to create new permit_query : permit_query_new

    path('new/', views.PermitQueryCreateView.as_view(), name='permit_query_new'),

    # Path to edit permit_query : edit_list

    path('<int:pk>/edit', views.PermitQueryUpdateView.as_view(), name='permit_query_edit'),

    # Path to delete permit_query : permit_query_delete

    path('<int:pk>/delete', views.PermitQueryDeleteView.as_view(), name='permit_query_delete'),

    # Path to detail view of permit_query : permit_query_details

    path('<int:pk>', views.PermitQueryDetailView.as_view(), name='permit_query_details')
]
