
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of helpQna : helpQna_list

    path('', views.helpQnaListView.as_view(), name='helpQna_list'),

    # Path to create new helpQna : helpQna_new

    path('new/', views.helpQnaCreateView.as_view(), name='helpQna_new'),

    # Path to edit helpQna : edit_list

    path('<int:pk>/edit', views.helpQnaUpdateView.as_view(), name='helpQna_edit'),

    # Path to delete helpQna : helpQna_delete

    path('<int:pk>/delete', views.helpQnaDeleteView.as_view(), name='helpQna_delete'),

    # Path to detail view of helpQna : helpQna_details

    path('<int:pk>', views.helpQnaDetailView.as_view(), name='helpQna_details')
]
