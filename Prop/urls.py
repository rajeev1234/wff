
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Prop_Amenitie : Prop_list

    path('', views.PropListView.as_view(), name='Prop_list'),

    # Path to create new Prop : Prop_new

    path('new/', views.PropCreateView.as_view(), name='Prop_new'),

    # Path to edit Prop : edit_list

    path('<int:pk>/edit', views.PropUpdateView.as_view(), name='Prop_edit'),

    # Path to delete Prop : Prop_delete

    path('<int:pk>/delete', views.PropDeleteView.as_view(), name='Prop_delete'),

    # Path to detail view of Prop : Prop_details

    path('<int:pk>', views.PropDetailView.as_view(), name='Prop_details')
]
