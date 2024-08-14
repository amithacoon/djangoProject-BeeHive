import io
import os
import sys

import pandas as pd
import csv
from django.shortcuts import render, HttpResponse
from openpyxl.reader.excel import load_workbook
import google.generativeai as genai

from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import time

import os
import shutil
from django.shortcuts import render, HttpResponse
from .forms import UploadCSVForm
from google.api_core.exceptions import ResourceExhausted

prompt1 = "קח את הטקסט הבא בעברית וסכם את הרקע המקצועי והאישי של היזם/יזמים למשפט אחד."
prompt2 = "קח את הטקסט הבא בעברית וסכם את האתגר המרכזי והספציפי שהמיזם מנסה לפתור בשני משפטים."
prompt3 = "קח את הטקסט הבא בעברית ותאר כיצד המיזם נותן מענה טכנולוגי או אסטרטגי לאתגר הספציפי בשני משפטים."
prompt4 = "קח את הסיכומים הבאים וכתוב סיכום חדש על המיזם באורך של עד 120 מילים. תן דגש לתכנית הפעולה או השלבים הבאים במיזם לקראת הסוף. אם שם המיזם לא מופיע בטקסט, קרא לו 'המיזם'."
prompt5 = "קח את הטקסט הבא בעברית וסכם את ההישגים או השלבים המרכזיים שנעשו עד היום במיזם למשפט אחד של עד 30 מילים."
prompt6 = "קח את הסיכומים הבאים וכתוב סיכום חדש ותמציתי על המיזם, כולל המטרה העיקרית והיתרון המרכזי, למשפט אחד בעברית."

'gemini-1.5-flash'
'gemini-1.0-pro'
from google.api_core.exceptions import ResourceExhausted
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



def gemini(prompt, text):
    model_name = 'gemini-1.5-flash'
    model = genai.GenerativeModel(model_name)
    genai.configure(api_key='AIzaSyB4uUsH3kMKA2cIpe8z4z221Ow4XRz0rWI')
    combined = prompt + text

    while True:
        try:
            response = model.generate_content(combined)

            # בדיקה אם התגובה מכילה תוכן תקין
            if not response.candidates or not hasattr(response.candidates[0].content, 'parts') or not response.candidates[0].content.parts:
                logger.error("No valid content found in response")
                return str("-")  # החזרת None אם אין תוכן תקין

            text = response.candidates[0].content.parts[0].text
            return text

        except ResourceExhausted as e:
            logger.warning(f"ResourceExhausted: {e}. Waiting for 120 seconds before retrying...")
            time.sleep(120)  # המתנה של 120 שניות לפני ניסיון נוסף
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return str("-")  # החזרת None אם אין תוכן תקין



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

    if not data:
        return HttpResponse("No data found in file")

    headers = data[0]
    rows = data[1:]

    return render(request, 'display.html', {'headers': headers, 'rows': rows})

def display_csv_2(request, filename):
    file_path = os.path.join('media/download', filename)
    extension = os.path.splitext(file_path)[1].lower()

    if extension == '.csv':
        data = read_csv_file(file_path)
    elif extension in ['.xls', '.xlsx']:
        data = read_excel_file(file_path)
    else:
        return HttpResponse("Unsupported file type")

    if not data:
        return HttpResponse("No data found in file")

    headers = data[0]
    rows = data[1:]

    return render(request, 'display.html', {'headers': headers, 'rows': rows})

def read_csv_file(file_path):
    data = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
    except Exception as e:
        return HttpResponse(f"Error reading CSV file: {e}")
    return data


def read_excel_file(file_path):
    try:
        df = pd.read_excel(file_path)
        data = df.values.tolist()
        headers = df.columns.tolist()
        data.insert(0, headers)  # Ensure headers are the first row
    except Exception as e:
        return HttpResponse(f"Error reading Excel file: {e}")
    return data

# Set standard output to use UTF-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

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

    # Apply RTL override for CSV if required
    if rtl and format.lower() == 'csv':
        rlo = '\u202E'
        df = df.applymap(lambda x: rlo + str(x) if isinstance(x, str) else x)

    if format.lower() == 'csv':
        full_filename = filename + '.csv'
        df.to_csv(full_filename, index=False, encoding='utf-8-sig')
        print(f"DataFrame saved as {full_filename} with UTF-8 encoding and RTL orientation")
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

def score_Bashlot(df, result_df):
    results = []
    total_rows = len(df) - 1
    from datetime import datetime
    import socket

    # קבלת התאריך של היום
    today_date = datetime.now().strftime("%Y-%m-%d")

    prompt_start_date = f"""
    The following text represents a date. Today's date is {today_date} and the date the project founded is:
    Return the corresponding score based on how long ago the date was:
    1 - Up to 6 months ago
    2 - above 6 months and under 12 months ago
    3 - above 1 and under 2 years ago
    4 - above 2 and under 4 years ago
    5 - above 4 years ago
    0 - If none of the above options match
    Return only the score as a number, nothing else. - here is the starting date : 
    """
    prompt_people_experienced = """
    For the following text, return the score based on how many people have tried the service:
    1 - 0 to 2 people
    2 - 3 to 12 people
    3 - 13 to 100 people
    4 - 101 to 1000 people
    5 - 1000 people and above
    0 - If none of the above options match
    Return only the score as a number.
    """

    prompt_salaried_employees = """
    The following text contains a value that could be an integer or a string. Please return the corresponding score:
    1 - If the value is 0
    2 - If the value is 1
    3 - If the value is in the range [2-3]
    4 - If the value is in the range [4-10]
    5 - If the value is 11 or above
    0 - If none of the above options match
    Return only the score as a number.
    """

    prompt_funds_raised = """
    For the following text, return the score based on the amount of budget the project has:
    1 - 0 budget
    2 - Up to 30,000
    3 - Between 30,001 and 100,000
    4 - Between 101,000 and 500,000
    5 - 500,000 and above
    0 - If none of the above options match
    Return only the score as a number.
    """

    prompt_project_maturity = """
    Analyze the following text to determine the maturity level of the project based on its current stage. Assign a score according to the following criteria:
    1 - The project is in the idea stage.
    2 - The project has an MVP (Minimum Viable Product).
    3 - The project is in the pilot stage.
    4 - The project has established regular customers.
    5 - The project has national impact and operates at a wide scale.
    Return only the score as a number, nothing else. 
    """

    for i in range(len(df)):
        text1 = str(df.iloc[i, 1])
        try:
            date = int(gemini(prompt_start_date, text1))
        except ValueError:
            date = 2.5
            print("Date Score (from text1): 2.5 (Default due to ValueError)")

        # time.sleep(13)

        text2 = str(df.iloc[i, 5])
        try:
            tried = int(gemini(prompt_people_experienced, text2))
        except ValueError:
            tried = 2.5
            print("People Experienced Score (from text2): 2.5 (Default due to ValueError)")

        # time.sleep(13)

        text3 = str(df.iloc[i, 8])
        try:
            employ = int(gemini(prompt_salaried_employees, text3))
        except ValueError:
            employ = 2.5
            print("Salaried Employees Score (from text3): 2.5 (Default due to ValueError)")

        # time.sleep(13)

        text4 = str(df.iloc[i, 9])
        try:
            money = int(gemini(prompt_funds_raised, text4))
        except ValueError:
            money = 2.5
            print("Funds Raised Score (from text4): 2.5 (Default due to ValueError)")

        # time.sleep(13)

        text5 = str(df.iloc[i, 11] + df.iloc[i, 12] + df.iloc[i, 14] + df.iloc[i, 15] + df.iloc[i, 16])
        try:
            percentage = int(gemini(prompt_project_maturity, text5))
        except ValueError:
            percentage = 2.5

        # time.sleep(6)

        result = 0.1 * date + 0.3 * tried + 0.1 * employ + 0.15 * money + 0.25 * percentage
        formatted_result = f"{result:.2f}"
        # time.sleep(20)
        results.append(formatted_result)

    new_column_df = pd.DataFrame(results, columns=["ציון בשלות"])
    result_df = df.join(new_column_df)
    return result_df




def process_dataframe_summary(df, result_df=None):
    results = []
    total_rows = len(df) - 1

    for i in range(len(df)):
        text = str(df.iloc[i, 10])
        answer1 = gemini(prompt2, text)
        text2 = str(df.iloc[i, 11])
        answer2 = gemini(prompt3, text2)
        text3 = str(df.iloc[i, 15])
        answer3 = gemini(prompt5, text3)
        text4 = " הסיכומים הינם " + answer1 + answer2 + answer3
        answer4 = gemini(prompt4, text4)
        results.append(answer4)

        # Log progress to Django console
        logger.info(f"Summary for row {i + 1}/{total_rows + 1} has been completed.")

    newname = "סיכום בפסקה"
    new_column_df = pd.DataFrame(results, columns=[newname])

    if result_df is None:
        result_df = pd.DataFrame(index=df.index)

    result_df = result_df.join(new_column_df)
    return result_df

def process_dataframe_summary_one_line(df, result_df=None):
    results = []
    total_rows = len(df) - 1

    for i in range(len(df)):
        try:
            text3 = str(df.iloc[i, 16])
            answer4 = gemini(prompt6, text3)
            results.append(answer4)
            logger.info(f"Summary in one line -  row {i + 1}/{total_rows + 1} has been completed.")
        except Exception as e:
            logger.error(f"Error processing row {i + 1}: {e}")
            results.append(None)  # או שתוכל לבחור להוסיף ערך דיפולטי במקרה של שגיאה

    newname = "סיכום בשורה"
    new_column_df = pd.DataFrame(results, columns=[newname])

    if result_df is None:
        result_df = pd.DataFrame(index=df.index)

    result_df = result_df.join(new_column_df)
    return result_df

def get_tags_activity(df, result_df=None):
    results = []
    tag_list = ["תעסוקה", "מוביליות חברתית", "חינוך והשכלה", "בריאות נפשית", "בריאות", "אחר", "קהילה"]

    for i in range(len(df)):
        try:
            text = str(df.iloc[i, 10])
            prompt = f"Given the next Hebrew text: '{text}', which of these tags is the best match? {tag_list}. Return only the tag and nothing else, return one!."
            answer = gemini(prompt, text)
            results.append(answer)
            logger.info(f"Tag for activity in row {i + 1}/{len(df)} has been completed.")
        except Exception as e:
            logger.error(f"Error processing row {i + 1}: {e}")
            results.append(None)

    newname = "תג - תחום חברתי"
    new_column_df = pd.DataFrame(results, columns=[newname])

    if result_df is None:
        result_df = pd.DataFrame(index=df.index)

    result_df = result_df.join(new_column_df)
    return result_df

def get_tags_age(df, result_df=None):
    results = []
    tag_list = ["הגיל הרך", "ילדים ונוער", "צעירים", "הזדקנות מיטבית, אנשים מעל גיל 90", "אחר"]

    for i in range(len(df)):
        try:
            text = str(df.iloc[i, 10])
            prompt = f"Given the next Hebrew text: '{text}', which of these tags is the best match? {tag_list}. Return only the tag and nothing else, return one!."
            answer = gemini(prompt, text)
            results.append(answer)
            logger.info(f"Tag for age group in row {i + 1}/{len(df)} has been completed.")
        except Exception as e:
            logger.error(f"Error processing row {i + 1}: {e}")
            results.append(None)

    newname = "תג - קבוצת גיל"
    new_column_df = pd.DataFrame(results, columns=[newname])

    if result_df is None:
        result_df = pd.DataFrame(index=df.index)

    result_df = result_df.join(new_column_df)
    return result_df

def get_tags_population(df, result_df=None):
    results = []
    tag_list = ["החברה הערבית", "החברה החרדית", 'קהילת הלהט"ב', "קהילת יוצאי אתיופיה",
                "אוכלוסיות בסיכון ומצבי קצה", "אנשים עם מוגבלות", "אחר"]

    for i in range(len(df)):
        try:
            text = str(df.iloc[i, 16])
            prompt = f"Given the next Hebrew text: '{text}', which of these tags is the best match? {tag_list}. Return only the tag and nothing else, return one!."
            answer = gemini(prompt, text)
            results.append(answer)
            logger.info(f"Tag for population in row {i + 1}/{len(df)} has been completed.")
        except Exception as e:
            logger.error(f"Error processing row {i + 1}: {e}")
            results.append(None)

    newname = "תג - אוכלסיית יעד"
    new_column_df = pd.DataFrame(results, columns=[newname])

    if result_df is None:
        result_df = pd.DataFrame(index=df.index)

    result_df = result_df.join(new_column_df)
    return result_df



def score_Hadash(df, result_df=None):
    results = []
    total_rows = len(df) - 1

    prompt_start_date = """
    קרא את המיזם הבא ותן לו דירוג מ-1 עד 5 על פי מידת החדשנות שלו ביחס למיזמים אחרים בתחום שנותנים מענה לאותה בעיה.
    החזר את התשובה במספר בלבד.
    """

    for i in range(len(df)):
        try:
            text1 = str(df.iloc[i, 16])
            date = gemini(prompt_start_date, text1)
            logger.info(f"Processed row {i + 1}/{total_rows + 1}: Innovation score")

            formatted_result = date
            results.append(formatted_result)
        except Exception as e:
            logger.error(f"Error processing row {i + 1}: {e}")
            results.append(None)

    new_column_df = pd.DataFrame(results, columns=["ציון חדשנות"])

    if result_df is None:
        result_df = pd.DataFrame(index=df.index)

    result_df = result_df.join(new_column_df)
    return result_df


def score_Hadash2(df, result_df=None):
    results = []
    total_rows = len(df) - 1

    prompt_start_date2 = """
    קח את הטקסט הבא ופרט בצורה מקצועית את הסיבות לכך שהוא חדשני ביחס למיזמים דומים שאתה מכיר במקורות שלך, מבחינת הבעיה שהמיזם פותר. השתמש במידע מהאינטרנט ללא אזכור כתובות של אתרים, והחזר את התשובה בתגיות שמייצגות את הסיבות לחדשנות, עד 3 תגיות מופרדות בפסיקים, וכל סיבה בתגית יכולה לכלול עד 20 מילים. כל התוכן צריך להיות בטקסט, ללא כותרות.
    """

    for i in range(len(df)):
        try:
            text1 = str(df.iloc[i, 16])
            date = gemini(prompt_start_date2, text1)
            logger.info(f"Processed row {i + 1}/{total_rows + 1}: Reasons for innovation")

            results.append(date)
        except Exception as e:
            logger.error(f"Error processing row {i + 1}: {e}")
            results.append(None)

    new_column_df = pd.DataFrame(results, columns=["סיבות לחדשנות"])

    if result_df is None:
        result_df = pd.DataFrame(index=df.index)

    result_df = result_df.join(new_column_df)
    return result_df


import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google.api_core.exceptions import ResourceExhausted



@csrf_exempt
def run_df(request):
    if request.method == 'POST':
        start_time = time.time()

        file = request.FILES.get('csv_file')
        if not file:
            return JsonResponse({'error': 'No file uploaded'}, status=400)

        format = request.POST.get('format', 'csv')
        file_path = f'media/{file.name}'
        handle_uploaded_file(file)

        df = load_excel_to_dataframe(file_path)
        if df is None:
            return JsonResponse({'error': 'Failed to load file into DataFrame'}, status=400)

        # הרצת תהליך עיבוד הנתונים
        # לאחר כל שלב בעיבוד ה-DataFrame נוסיף הודעה שמדפיסה למסוף

        df1 = process_dataframe_summary(df, df)
        logger.info("Completed processing df1: process_dataframe_summary")

        df2 = process_dataframe_summary_one_line(df1, df1)
        logger.info("Completed processing df2: process_dataframe_summary_one_line")

        df3 = get_tags_activity(df2, df2)
        logger.info("Completed processing df3: get_tags_activity")

        df5 = get_tags_population(df3, df3)
        logger.info("Completed processing df5: get_tags_population")

        df6 = score_Bashlot(df5, df5)
        logger.info("Completed processing df6: score_Bashlot")

        df7 = score_Hadash(df6, df6)
        logger.info("Completed processing df7: score_Hadash")

        df8 = score_Hadash2(df7, df7)
        logger.info("Completed processing df8: score_Hadash2")

        # שמירת ה-DataFrame
        save_dataframe(df8, format=format)

        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"run_df execution time: {execution_time} seconds")

        filename = f'Updated_Table.{format}'
        download_url = f'/media/download/{filename}'
        return JsonResponse({'result': '', 'download_url': download_url, 'execution_time': execution_time, 'filename': filename})

    return JsonResponse({'error': 'Invalid request'}, status=400)
