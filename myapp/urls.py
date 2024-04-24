from django.urls import path
from .views import csv_upload_view, display_csv

urlpatterns = [
    path('upload/', csv_upload_view, name='upload-csv'),
    path('display-csv/<str:filename>/', display_csv, name='display-csv'),
]
