
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of UserCoinBox : UserCoinBox_list

    path('', views.UserCoinBoxListView.as_view(), name='UserCoinBox_list'),

    # Path to create new UserCoinBox : UserCoinBox_new

    path('new/', views.UserCoinBoxCreateView.as_view(), name='UserCoinBox_new'),

    # Path to edit UserCoinBox : edit_list

    path('<int:pk>/edit', views.UserCoinBoxUpdateView.as_view(), name='UserCoinBox_update'),

    # Path to delete UserCoinBox : UserCoinBox_delete

    path('<int:pk>/delete', views.UserCoinBoxDeleteView.as_view(), name='UserCoinBox_delete'),

    # Path to detail view of UserCoinBox : UserCoinBox_details

    path('<int:pk>', views.UserCoinBoxDetailView.as_view(), name='UserCoinBox_details')
]
