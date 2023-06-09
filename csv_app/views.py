import csv
from django.shortcuts import render
from django.contrib import messages
from .forms import CSVUploadForm
from .models import User

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            total_data = 0
            total_success = 0
            total_duplicate = 0
            total_invalid = 0
            total_incomplete = 0
            for row in reader:
                total_data += 1
                name = row['name']
                email = row['email']
                phone_number = row['phone_number']
                gender = row['gender']
                address = row['address']
                if not all([name, email, phone_number, gender, address]):
                    total_incomplete += 1
                    continue
                if User.objects.filter(email=email).exists() or User.objects.filter(phone_number=phone_number).exists():
                    total_duplicate += 1
                    continue
                if not is_valid_bangladeshi_phone_number(phone_number):
                    total_invalid += 1
                    continue
                User.objects.create(name=name, email=email, phone_number=phone_number, gender=gender, address=address)
                total_success += 1
            messages.success(request, 'CSV file uploaded successfully.')
            summary = {
                'total_data': total_data,
                'total_success': total_success,
                'total_duplicate': total_duplicate,
                'total_invalid': total_invalid,
                'total_incomplete': total_incomplete
            }
            return render(request, 'csv_app/upload_csv.html', {'form': form, 'summary': summary})
    else:
        form = CSVUploadForm()
    return render(request, 'csv_app/upload_csv.html', {'form': form})

import re

def is_valid_bangladeshi_phone_number(phone_number):
    # Remove any whitespace or special characters from the phone number
    cleaned_phone_number = re.sub(r'\s+|-', '', phone_number)

    # Validate the phone number using a regex pattern for Bangladeshi numbers
    pattern = r'^\+?(88)?0?1[3456789][0-9]{8}$'
    is_valid = re.match(pattern, cleaned_phone_number) is not None

    return is_valid

from django.db.models import Q

from django.db.models import Q

from django.db.models import Q
from django.shortcuts import redirect

from django.db.models import Q

def list_users(request):
    query = request.GET.get('q', '')
    filter_name = request.GET.get('name', '')
    filter_email = request.GET.get('email', '')
    filter_phone_number = request.GET.get('phone_number', '')
    filter_gender = request.GET.get('gender', '')
    filter_address = request.GET.get('address', '')

    users = User.objects.all()

    if filter_name:
        users = users.filter(name__icontains=filter_name)
    if filter_email:
        users = users.filter(email__icontains=filter_email)
    if filter_phone_number:
        users = users.filter(phone_number__icontains=filter_phone_number)
    if filter_address:
        users = users.filter(address__icontains=filter_address)

    if filter_gender:
        users = users.filter(gender__iexact=filter_gender)

    if query:
        users = users.filter(name__icontains=query)

    return render(request, 'csv_app/list_users.html', {'users': users, 'query': query})