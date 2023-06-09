from django.urls import path
from csv_app.views import upload_csv, list_users, delete_user

urlpatterns = [
    path('upload-csv/', upload_csv, name='upload_csv'),
    path('list-users/', list_users, name='list_users'),
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
]