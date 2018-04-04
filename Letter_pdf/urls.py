
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Letter_pdf : Letter_pdf_list

    path('', views.Letter_pdfListView.as_view(), name='Letter_pdf_list'),

    # Path to create new Letter_pdf : Letter_pdf_new

    path('new/', views.Letter_pdfCreateView.as_view(), name='Letter_pdf_new'),

    # Path to edit Letter_pdf : edit_list

    path('<int:pk>/edit', views.Letter_pdfUpdateView.as_view(), name='Letter_pdf_edit'),

    # Path to delete Letter_pdf : Letter_pdf_delete

    path('<int:pk>/delete', views.Letter_pdfDeleteView.as_view(), name='Letter_pdf_delete'),

    # Path to detail view of Letter_pdf : Letter_pdf_details

    path('<int:pk>', views.Letter_pdfDetailView.as_view(), name='Letter_pdf_details')
]
