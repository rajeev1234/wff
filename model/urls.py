
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Model : Model_list

    path('', views.ModelsListView.as_view(), name='Model_list'),

    # Path to create new Model : Model_new

    path('new/', views.ModelsCreateView.as_view(), name='Model_new'),

    # Path to edit Model : edit_list

    path('<int:pk>/edit', views.ModelsUpdateView.as_view(), name='Model_edit'),

    # Path to delete Model : Model_delete

    path('<int:pk>/delete', views.ModelsDeleteView.as_view(), name='Model_delete'),

    # Path to detail view of Model : Model_details

    path('<int:pk>', views.ModelsDetailView.as_view(), name='Model_details')
]
