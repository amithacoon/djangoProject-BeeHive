from django.urls import path
from .views import csv_upload_view, display_csv, run_df, get_progress_view

urlpatterns = [
    path('', csv_upload_view, name='upload-csv'),
    path('display-csv/<str:filename>/', display_csv, name='display-csv'),
    path('run_df/', run_df, name='run_df'),
    path('get_progress/', get_progress_view, name='get_progress'),  # New progress endpoint
]
