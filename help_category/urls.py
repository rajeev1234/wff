
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of helpcategory : helpcategory_list

    path('', views.Help_CategoryListView.as_view(), name='helpcategory_list'),

    # Path to create new helpcategory : helpcategory_new

    path('new/', views.Help_CategoryCreateView.as_view(), name='helpcategory_new'),

    # Path to edit helpcategory : edit_list

    path('<int:pk>/edit', views.Help_CategoryUpdateView.as_view(), name='helpcategory_edit'),

    # Path to delete helpcategory : helpcategory_delete

    path('<int:pk>/delete', views.Help_CategoryDeleteView.as_view(), name='helpcategory_delete'),

    # Path to detail view of helpcategory : helpcategory_details

    path('<int:pk>', views.Help_CategoryDetailView.as_view(), name='helpcategory_details')
]
