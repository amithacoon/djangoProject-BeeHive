import os
import pandas as pd
import csv
from django.shortcuts import render, HttpResponse
from openpyxl.reader.excel import load_workbook
import google.generativeai as genai
from .forms import UploadCSVForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time

def gemini(prompt, text):
    model_name = 'gemini-1.5-flash'  # Replace with an available model name if needed
    model = genai.GenerativeModel(model_name)
    genai.configure(api_key='AIzaSyB3h0w_rzHYiaFDP6PJ5VqiBw3l8sKF3hA')
    combined =prompt + text
    response = model.generate_content(combined)
    text = response.candidates[0].content.parts[0].text
    return (text)


prompt1 = "קח את הטקסט הבא בעברית וסכם את הרקע של היזם/יזמים למשפט אחד."

import os
import shutil
from django.shortcuts import render, HttpResponse
from .forms import UploadCSVForm

def clear_media_directory():
    media_dir = 'media/'
    if os.path.exists(media_dir):
        shutil.rmtree(media_dir)  # Remove the directory and all its contents
    os.makedirs(media_dir)  # Create a new empty directory

def handle_uploaded_file(f):
    with open(f'media/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def csv_upload_view(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            clear_media_directory()  # Clear the media directory before uploading the new file
            file = request.FILES['csv_file']
            handle_uploaded_file(file)
            return display_csv(request, file)
    else:
        form = UploadCSVForm()
    return render(request, 'home.html', {'form': form})

def handle_uploaded_file(f):
    with open(f'media/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def display_csv(request, f):
    file_path = f'media/{f.name}'
    extension = os.path.splitext(file_path)[1].lower()

    if extension == '.csv':
        data = read_csv_file(file_path)
    elif extension in ['.xls', '.xlsx']:
        data = read_excel_file(file_path)
    else:
        return HttpResponse("Unsupported file type")

    return render(request, 'display.html', {'data': data})


def read_csv_file(file_path):
    data = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
    except Exception as e:
        return HttpResponse(f"Error reading CSV file: {e}")
    return data


def read_excel_file(file_path):
    try:
        df = pd.read_excel(file_path)  # pandas can read directly from Excel files
        data = df.values.tolist()  # Convert DataFrame to list of lists for the template
    except Exception as e:
        return HttpResponse(f"Error reading Excel file: {e}")
    return data


def load_excel_to_dataframe(file_path):
    """
    Load an Excel file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the Excel file.

    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        print("Excel file loaded successfully!")
        return df
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None


import threading

progress_lock = threading.Lock()
progress = 0


def update_progress(value):
    global progress
    with progress_lock:
        progress = value


def get_progress():
    global progress
    with progress_lock:
        return progress


def process_dataframe(df, column_number, newname, prompt1, result_df=None):
    global progress
    results = []
    total_rows = len(df) - 1

    for i in range(1, len(df)):
        text = str(df.iloc[i, column_number])
        result = gemini(prompt1, text)
        results.append(result)

        # Update progress
        update_progress((i / total_rows) * 100)

    new_column_df = pd.DataFrame(results, columns=[newname])

    if result_df is None:
        result_df = pd.DataFrame(index=df.index)

    result_df = result_df.join(new_column_df)
    return result_df


from django.http import JsonResponse

def get_progress_view(request):
    return JsonResponse({'progress': get_progress()})


def asis_df(df, column_number, newname, result_df=None):
    # Initialize an empty list to store results
    results = []

    # Extract the text from the specified column
    for i in range(1, len(df)):
        text = str(df.iloc[i, column_number])
        results.append(text)

    # Create a new DataFrame from the results list
    new_column_df = pd.DataFrame(results, columns=[newname])

    # If result_df is not provided, create a new DataFrame with the same index as df
    if result_df is None:
        result_df = pd.DataFrame(index=df.index)

    # Add the new column to the result DataFrame
    result_df = result_df.join(new_column_df)

    return result_df


def save_dataframe(df, format, rtl=True):
    directory = 'media/download'
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = os.path.join(directory, 'Updated_Table')

    if format.lower() == 'csv':
        full_filename = filename + '.csv'
        df.to_csv(full_filename, index=False)
        print(f"DataFrame saved as {full_filename}")
    elif format.lower() == 'xlsx':
        full_filename = filename + '.xlsx'
        df.to_excel(full_filename, index=False)
        if rtl:
            # Load the workbook and select the active sheet
            wb = load_workbook(full_filename)
            ws = wb.active

            # Set the sheet to RTL orientation
            ws.sheet_view.rightToLeft = True

            # Save the modified workbook with RTL support
            wb.save(full_filename)
            print(f"DataFrame saved as {full_filename} with RTL orientation")
        else:
            print(f"DataFrame saved as {full_filename}")
    else:
        raise ValueError("Unsupported format. Please choose either 'csv' or 'xlsx'.")
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import time

@csrf_exempt
def run_df(request):
    if request.method == 'POST':
        file = request.FILES.get('csv_file')
        if not file:
            return JsonResponse({'error': 'No file uploaded'}, status=400)

        format = request.POST.get('format', 'csv')
        file_path = f'media/{file.name}'
        handle_uploaded_file(file)

        # Load the file into a DataFrame
        df = load_excel_to_dataframe(file_path)

        if df is None:
            return JsonResponse({'error': 'Failed to load file into DataFrame'}, status=400)

        # Process the DataFrame
        df =  process_dataframe(df, 6, 'תקציר על יזם', prompt1)  # Modify as needed

        # Save the DataFrame
        save_dataframe(df, format=format)

        download_url = f'../media/download/Updated_Table.{format}'
        return JsonResponse({'result': '', 'download_url': download_url})
    return JsonResponse({'error': 'Invalid request'}, status=400)

