
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of comments : comments_list

    path('', views.CommentsListView.as_view(), name='comments_list'),

    # Path to create new comments : comments_new

    path('new/', views.CommentsCreateView.as_view(), name='comments_new'),

    # Path to edit comments : edit_list

    path('<int:pk>/edit', views.CommentsUpdateView.as_view(), name='comments_edit'),

    # Path to delete comments : comments_delete

    path('<int:pk>/delete', views.CommentsDeleteView.as_view(), name='comments_delete'),

    # Path to detail view of comments : comments_details

    path('<int:pk>', views.CommentsDetailView.as_view(), name='comments_details')
]
