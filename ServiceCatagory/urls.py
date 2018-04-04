
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of ServiceCatagory : ServiceCatagory_list

    path('', views.ServiceCatagoryListView.as_view(), name='ServiceCatagory_list'),

    # Path to create new ServiceCatagory : ServiceCatagory_new

    path('new/', views.ServiceCatagoryCreateView.as_view(), name='ServiceCatagory_new'),

    # Path to edit ServiceCatagory : edit_list

    path('<int:pk>/edit', views.ServiceCatagoryUpdateView.as_view(), name='ServiceCatagory_update'),

    # Path to delete ServiceCatagory : ServiceCatagory_delete

    path('<int:pk>/delete', views.ServiceCatagoryDeleteView.as_view(), name='ServiceCatagory_delete'),

    # Path to detail view of ServiceCatagory : ServiceCatagory_details

    path('<int:pk>', views.ServiceCatagoryDetailView.as_view(), name='ServiceCatagory_details')
]
