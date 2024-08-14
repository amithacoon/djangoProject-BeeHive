import io
import os
import sys
import logging
import sys
import io
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
import logging

# Configure logging (if not already done)
# Configure logging to both file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('myapp.log', encoding='utf-8'),  # Log to a file with UTF-8 encoding
        logging.StreamHandler()  # Log to the console (using the default encoding for the console)
    ]
)

logger = logging.getLogger(__name__)

# New view to serve log content
import re

def show_logs(request):
    log_file_path = 'myapp.log'  # Path to the log file
    http_request_logs = []

    # Regular expression to match HTTP request logs
    http_request_pattern = re.compile(r'\"(GET|POST|PUT|DELETE|PATCH) .+\" \d{3} \d+')

    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                if http_request_pattern.search(line):
                    http_request_logs.append(line)
        log_content = ''.join(http_request_logs)
        return HttpResponse(log_content, content_type='text/plain')
    else:
        return HttpResponse("Log file not found.", content_type='text/plain')









prompt1 = (
    "קח את הטקסט הבא בעברית וסכם את הרקע המקצועי והאישי של היזם או היזמים בצורה קצרה וממוקדת. "
    "השתמש במשפט אחד ברור וממוקד שמכיל מידע מרכזי בלבד על הניסיון המקצועי וההכשרות האישיות הרלוונטיות שלהם. "
    "אנא הימנע מפרטים שוליים והתרכז רק בנקודות המפתח שיכולות לתרום להבנת היכולות של היזם בתחום זה. "
    "החזר את התשובה בעברית בלבד וללא סימנים מיוחדים כמו * או #."
)

prompt2 = (
    "קח את הטקסט הבא בעברית וסכם את האתגר המרכזי והספציפי שהמיזם מנסה לפתור. "
    "נסח שני משפטים קצרים וברורים שמתארים את הבעיה המרכזית שהמיזם מתמודד איתה. "
    "על המשפטים להתרכז בהיבטים הקריטיים של האתגר, תוך הדגשה מדוע הוא חשוב לתחום בו פועל המיזם. "
    "אין לכלול תיאורים כלליים, רק פרטים מדויקים ונקודתיים. "
    "החזר את התשובה בעברית בלבד וללא סימנים מיוחדים כמו * או #."
)

prompt3 = (
    "קח את הטקסט הבא בעברית ופרט כיצד המיזם מציע פתרון טכנולוגי או אסטרטגי לאתגר הספציפי. "
    "כתוב שני משפטים שמדגישים את האסטרטגיה המרכזית או את הפתרון הטכנולוגי המרכזי שהמיזם מציע, "
    "תוך התמקדות בחדשנות ובייחודיות של הגישה שנבחרה. על התיאור להיות ממוקד ומבוסס על יתרונות מעשיים של המיזם. "
    "החזר את התשובה בעברית בלבד וללא סימנים מיוחדים כמו * או #."
)

prompt4 = (
    "סכם את המידע המופיע בטקסטים הבאים וכתוב תיאור חדש וממוקד של המיזם באורך של לפחות 150 מילים. "
    "על התיאור להדגיש את תכנית הפעולה או השלבים הבאים שהמיזם מתכנן ליישם, "
    "תוך התמקדות בהתפתחויות העתידיות והאתגרים המרכזיים שעדיין נדרשים להתמודדות. "
    "במידה ושם המיזם אינו מופיע בטקסט, השתמש במונח 'המיזם' במקום שם ספציפי. "
    "החזר את התשובה בעברית בלבד וללא סימנים מיוחדים כמו * או #."
)


prompt5 = (
    "קח את הטקסט הבא בעברית וסכם בצורה מדויקת את ההישגים המרכזיים או השלבים העיקריים שהושגו עד היום במיזם. "
    "נסח משפט אחד, של לפחות 30 מילים, המתאר בקצרה ובאופן ממוקד את ההתקדמות וההישגים הבולטים ביותר של המיזם. "
    "שים דגש על תוצאות ממשיות או צעדים חשובים שנעשו בדרך להגשמת מטרות המיזם. "
    "החזר את התשובה בעברית בלבד וללא סימנים מיוחדים כמו * או #."
)

prompt6 = (
    "קח את הסיכומים הבאים וכתוב סיכום חדש וממוקד על המיזם, המדגיש את המטרה העיקרית והיתרון המרכזי שלו. "
    "נסח משפט אחד בעברית המשלב את שני האלמנטים הללו בצורה תמציתית וברורה. "
    "המשפט צריך לשקף את הערך המוסף של המיזם ואת הייחודיות שלו בתחום בו הוא פועל. "
    "החזר את התשובה בעברית בלבד וללא סימנים מיוחדים כמו * או #."
)

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
        name= str(df.iloc[i, 0])
        text = str(df.iloc[i, 10])
        answer1 = gemini(prompt2, text)
        text2 = str(df.iloc[i, 11])
        answer2 = gemini(prompt3, text2)
        text3 = str(df.iloc[i, 15])
        answer3 = gemini(prompt5, text3)
        text4 =  "שם המיזם הינו - " + name +  " הסיכומים הינם " + answer1 + answer2 + answer3
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
    # הגדרת מילות המפתח לכל תג
    keywords = {
        "תעסוקה": ["תעסוקה", "משק", "קריירה", "עבודה", "מובטלים", "אבטלה", "שכר", "הכשרה", "קישורים"],
        "חוסן כלכלי": ["חובות", "כלכלי", "עוני", "פערים חברתיים", "סוציו-אקונומי"],
        "חינוך והשכלה": ["אוריינות", "דיגיטלית", "Stem", "השכלה", "חינוך", "בית ספר", "אקדמיה"],
        "בריאות נפשית": ["נפש", "רגש", "דיכאון", "חרדה", "פוסט-טראומה", "הפרעות אכילה", "אובדנות", "התחזקות נפשית", "Mental"],
        "לכידות קהילתית": ["שכונה", "קהילה", "הון חברתי", "שייכות", "קבוצת שווים", "מועצות", "התנדבות", "ערבות הדדית"],
        "אלימות ופשיעה": ["התחמקות", "סמים", "אלימות", "פגיעה מינית", "ביזול", "עבירות", "חם"],
        "בריאות ושיקום פיזי": ["אורח חיים", "תזונה", "פגיעות גופניות", "חולי", "ספורט", "פיזיותרפיה"]
    }

    for i in range(len(df)):
        try:
            text = str(df.iloc[i, 10])
            found_tag = None

            # חיפוש המילים בטקסט והתאמת התג המתאים ממילות המפתח
            for tag, words in keywords.items():
                if any(word in text for word in words):
                    found_tag = tag
                    logger.info(f"Tag for activity in row {i + 1}/{len(df)} was found using keywords.")
                    break

            # אם לא נמצאה התאמה למילות המפתח, השתמש ב-GEMINI כדי להתאים תג
            if found_tag is None:
                prompt = f"Given the next Hebrew text: '{text}', which of these tags is the best match? {list(keywords.keys())}. Return only the tag and nothing else, return one!."
                found_tag = gemini(prompt, text)
                logger.info(f"Tag for activity in row {i + 1}/{len(df)} was found using GEMINI.")

            results.append(found_tag)
        except Exception as e:
            logger.error(f"Error processing row {i + 1}: {e}")
            results.append(None)

    newname = "תג - תחום חברתי"
    new_column_df = pd.DataFrame(results, columns=[newname])

    if result_df is None:
        result_df = pd.DataFrame(index=df.index)

    result_df = result_df.join(new_column_df)
    return result_df


def get_tags_population(df, result_df=None):
    results = []
    # הגדרת מילות המפתח לכל תג
    keywords = {
        "הגיל הרך": ["תינוקות", "פעוטות", "גני ילדים", "לידה"],
        "ילדים ונוער": ["בני נוער", "ילדים", "הורים", "בית ספר"],
        "צעירים": ["חיילים משוחררים", "צעירים", "ג'וניורים", "סטודנטים"],
        "זקנים": ["הגיל השלישי", "זקנים", "תחולת חיים", "פנסיה", "קשישים"],
        "החברה הערבית": ["בדואים", "ערבים", "דרוזים", "פזורה", "המשולש"],
        "החברה החרדית": ["חרדים", "כולל", "לימודי ליבה"],
        "אוכלוסיות מיעוטים נוספות": ["יוצאי אתיופיה", "עולים חדשים", "להט\"ב"],
        "אוכלוסיות במצבי קצה": ["אסירים משוחררים", "דרי רחוב", "זנות"],
        "אנשים עם מוגבלות": ["נכות", "מוגבלות", "חרשים", "עיוורים", "אוטיזם", "נפשי", "מוגבלים שכלית", "מוגבלות פיזית"]
    }

    for i in range(len(df)):
        try:
            text = str(df.iloc[i, 16])
            found_tag = None

            # חיפוש המילים בטקסט והתאמת התג המתאים ממילות המפתח
            for tag, words in keywords.items():
                if any(word in text for word in words):
                    found_tag = tag
                    logger.info(f"Tag for population in row {i + 1}/{len(df)} was found using keywords.")
                    break

            # אם לא נמצאה התאמה למילות המפתח, השתמש ב-GEMINI כדי להתאים תג
            if found_tag is None:
                prompt = f"Given the next Hebrew text: '{text}', which of these tags is the best match? {list(keywords.keys())}. Return only the tag and nothing else, return one!."
                found_tag = gemini(prompt, text)
                logger.info(f"Tag for population in row {i + 1}/{len(df)} was found using GEMINI.")

            results.append(found_tag)
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
    קח את הטקסט הבא ופרט בצורה מקצועית את הסיבות לכך שהוא חדשני ביחס למיזמים דומים שאתה מכיר במקורות שלך, מבחינת הבעיה שהמיזם פותר. השתמש במידע מהאינטרנט ללא אזכור כתובות של אתרים. החזר את התשובה בפורמט הבא:
    סיבה ראשונה: [סיבה ראשונה]
    סיבה שניה:  [סיבה שנייה]
וכדומה כמה שצריך. 
    יש להחזיר את התשובה בטקסט פשוט, ללא כותרות או תווים מיוחדים כמו * או #, ועד 20 מילים לכל סיבה. כל סיבה צריכה להיות בפסקה נפרדת.
    """

    for i in range(len(df)):
        try:
            text1 = str(df.iloc[i, 16])
            response_text = gemini(prompt_start_date2, text1)

            # הוספת '#' וירידת שורה אחרי כל סיבה
            for reason_number in ["ראשונה", "שניה", "שלישית", "רביעית", "חמישית", "שישית"]:
                response_text = response_text.replace(f"סיבה {reason_number}:", f"#סיבה {reason_number}:\n")

            logger.info(f"Processed row {i + 1}/{total_rows + 1}: Reasons for innovation")

            results.append(response_text)
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


# Import required modules for handling logs
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import time
import os

# Existing imports and setup...
# [Your existing code here]

# Configure logging (if not already done)
logging.basicConfig(
    filename='myapp.log',  # Log to a file called 'myapp.log'
    level=logging.INFO,  # Log level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
)
logger = logging.getLogger(__name__)

# New view to serve log content
def show_logs(request):
    log_file_path = 'myapp.log'  # Path to the log file

    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as log_file:
            log_content = log_file.read()
        return HttpResponse(log_content, content_type='text/plain')
    else:
        return HttpResponse("Log file not found.", content_type='text/plain')

# [Rest of your existing views like `run_df`, etc.]

# Example run_df with logger info
@csrf_exempt
def run_df(request):
    if request.method == 'POST':
        # Clear the log file
        open('myapp.log', 'w').close()  # This will empty the log file

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

        # DataFrame processing steps with logging
        df1 = process_dataframe_summary(df, df)
        logger.info("Completed processing: summary in paragraph")

        df2 = process_dataframe_summary_one_line(df1, df1)
        logger.info("Completed processing: summary in one line ")

        df3 = get_tags_activity(df2, df2)
        logger.info("Completed processing: social activity tag ")

        df5 = get_tags_population(df3, df3)
        logger.info("Completed processing: population target tag")

        df6 = score_Bashlot(df5, df5)
        logger.info("Completed processing: maturity score ")

        df7 = score_Hadash(df6, df6)
        logger.info("Completed processing: innovation score ")

        df8 = score_Hadash2(df7, df7)
        logger.info("Completed processing: reasons for innovation")

        # Save the DataFrame
        save_dataframe(df8, format=format)

        end_time = time.time()
        execution_time = end_time - start_time
        minutes, seconds = divmod(execution_time, 60)
        logger.info(f"Program execution time: {int(minutes)} minutes and {seconds:.2f} seconds")

        filename = f'Updated_Table.{format}'
        download_url = f'/media/download/{filename}'
        return JsonResponse(
            {'result': '', 'download_url': download_url, 'execution_time': execution_time, 'filename': filename})

    return JsonResponse({'error': 'Invalid request'}, status=400)
