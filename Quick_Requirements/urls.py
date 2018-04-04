
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Quick_Requirements_Amenitie : Quick_Requirements_list

    path('', views.Quick_RequirementsListView.as_view(), name='Quick_Requirements_list'),

    # Path to create new Quick_Requirements : Quick_Requirements_new

    path('new/', views.Quick_RequirementsCreateView.as_view(), name='Quick_Requirements_new'),

    # Path to edit Quick_Requirements : edit_list

    path('<int:pk>/edit', views.Quick_RequirementsUpdateView.as_view(), name='Quick_Requirements_edit'),

    # Path to delete Quick_Requirements : Quick_Requirements_delete

    path('<int:pk>/delete', views.Quick_RequirementsDeleteView.as_view(), name='Quick_Requirements_delete'),

    # Path to detail view of Quick_Requirements : Quick_Requirements_details

    path('<int:pk>', views.Quick_RequirementsDetailView.as_view(), name='Quick_Requirements_details')
]
