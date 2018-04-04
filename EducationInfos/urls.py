
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of EducationInfo : EducationInfo_list

    path('', views.EducationInfoListView.as_view(), name='EducationInfo_list'),

    # Path to create new EducationInfo : EducationInfo_new

    path('new/', views.EducationInfoCreateView.as_view(), name='EducationInfo_new'),

    # Path to edit EducationInfo : edit_list

    path('<int:pk>/edit', views.EducationInfoUpdateView.as_view(), name='EducationInfo_update'),

    # Path to delete EducationInfo : EducationInfo_delete

    path('<int:pk>/delete', views.EducationInfoDeleteView.as_view(), name='EducationInfo_delete'),

    # Path to detail view of EducationInfo : EducationInfo_details

    path('<int:pk>', views.EducationInfoDetailView.as_view(), name='EducationInfo_details')
]
