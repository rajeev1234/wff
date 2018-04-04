    
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Costume : Costume_list

    path('', views.CostumeListView.as_view(), name='Costume_list'),

    # Path to create new Costume : Costume_new

    path('new/', views.CostumeCreateView.as_view(), name='Costume_new'),

    # Path to edit Costume : edit_list

    path('<int:pk>/edit', views.CostumeUpdateView.as_view(), name='Costume_update'),

    # Path to delete Costume : Costume_delete

    path('<int:pk>/delete', views.CostumeDeleteView.as_view(), name='Costume_delete'),

    # Path to detail view of Costume : Costume_details

    path('<int:pk>', views.CostumeDetailView.as_view(), name='Costume_details')
]
