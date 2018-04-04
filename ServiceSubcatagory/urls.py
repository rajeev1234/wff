
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of ServiceSubcatagory : ServiceSubcatagory_list

    path('', views.ServiceSubcatagoryListView.as_view(), name='ServiceSubcatagory_list'),

    # Path to create new ServiceSubcatagory : ServiceSubcatagory_new

    path('new/', views.ServiceSubcatagoryCreateView.as_view(), name='ServiceSubcatagory_new'),

    # Path to edit ServiceSubcatagory : edit_list

    path('<int:pk>/edit', views.ServiceSubcatagoryUpdateView.as_view(), name='ServiceSubcatagory_update'),

    # Path to delete ServiceSubcatagory : ServiceSubcatagory_delete

    path('<int:pk>/delete', views.ServiceSubcatagoryDeleteView.as_view(), name='ServiceSubcatagory_delete'),

    # Path to detail view of ServiceSubcatagory : ServiceSubcatagory_details

    path('<int:pk>', views.ServiceSubcatagoryDetailView.as_view(), name='ServiceSubcatagory_details')
]
