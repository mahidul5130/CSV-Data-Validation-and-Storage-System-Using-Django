from django.urls import path
from csv_app.views import upload_csv, search_users

urlpatterns = [
    path('upload-csv/', upload_csv, name='upload_csv'),
    path('search-users/', search_users, name='search_users'),
]