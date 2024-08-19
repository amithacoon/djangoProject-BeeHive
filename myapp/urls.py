from django.urls import path
from .views import csv_upload_view, display_csv, run_df, get_progress_view, display_csv_2
from . import views


urlpatterns = [
    path('', csv_upload_view, name='upload-csv'),  # Ensure this is the correct view name
    path('display-csv/<str:filename>/', display_csv, name='display-csv'),
    path('display-csv-2/<str:filename>/', display_csv_2, name='display_csv_2'),
    path('run_df/', run_df, name='run_df'),
    path('get_progress/', get_progress_view, name='get_progress'),
    path('show_logs/', views.show_logs, name='show_logs'),
]
