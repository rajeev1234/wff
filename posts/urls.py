
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of post : post_list

    path('', views.PostListView.as_view(), name='post_list'),

    # Path to create new post : post_new

    path('new/', views.PostCreateView.as_view(), name='post_new'),

    # Path to edit post : edit_list

    path('<int:pk>/edit', views.PostUpdateView.as_view(), name='post_edit'),

    # Path to delete post : post_delete

    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),

    # Path to detail view of post : post_details

    path('<int:pk>', views.PostDetailView.as_view(), name='post_details')
]
