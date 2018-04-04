
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of helpsubcategory : helpsubcategory_list

    path('', views.helpsubcategoryListView.as_view(), name='helpsubcategory_list'),

    # Path to create new helpsubcategory : helpsubcategory_new

    path('new/', views.helpsubcategoryCreateView.as_view(), name='helpsubcategory_new'),

    # Path to edit helpsubcategory : edit_list

    path('<int:pk>/edit', views.helpsubcategoryUpdateView.as_view(), name='helpsubcategory_edit'),

    # Path to delete helpsubcategory : helpsubcategory_delete

    path('<int:pk>/delete', views.helpsubcategoryDeleteView.as_view(), name='helpsubcategory_delete'),

    # Path to detail view of helpsubcategory : helpsubcategory_details

    path('<int:pk>', views.helpsubcategoryDetailView.as_view(), name='helpsubcategory_details')
]
