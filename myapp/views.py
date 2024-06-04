from django.http import HttpResponse

from .forms import UploadCSVForm
import csv




def csv_upload_view(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['csv_file'])
            return display_csv(request, request.FILES['csv_file'])  # Ensure request is passed here
    else:
        form = UploadCSVForm()
    return render(request, 'home.html', {'form': form})


def handle_uploaded_file(f):
    with open(f'media/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def display_csv(request, f):
    file_path = f'media/{f.name}'
    data = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
    except Exception as e:
        return HttpResponse(f"Error reading CSV file: {e}")
    return render(request, 'display.html', {'data': data})


import pandas as pd
from django.shortcuts import render

def display_excel(request, f):
    file_path = f'media/{f.name}'
    df = pd.read_excel(file_path)  # pandas can read directly from Excel files
    data = df.values.tolist()  # Convert DataFrame to list of lists for the template
    return render(request, 'display.html', {'data': data})



import csv

