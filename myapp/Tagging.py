import time
import pandas as pd
import google.generativeai as genai
import os


# # File path
# input_csv_path = 'path/to/your/input.csv'
# output_csv_path = 'path/to/your/output.csv'

# Load the CSV data into a DataFrame
# df = pd.read_csv(input_csv_path, encoding='utf-8')

# Function to query OpenAI and get tag
class RequestLimitExceededError(Exception):
    pass
tag_list_activity = ["תעסוקה", "מוביליות חברתית", "חינוך והשכלה", "בריאות נפשית", "בריאות", "אחר", "קהילה"]
tag_list_age = ["הגיל הרך", "ילדים ונוער", "צעירים", "הזדקנות מיטבית, אנשים מעל גיל 90", "אחר"]
tag_list_population = ["החברה הערבית", "החברה החרדית", 'קהילת הלהט"ב', "קהילת יוצאי אתיופיה",
                       "אוכלוסיות בסיכון ומצבי קצה", "אנשים עם מוגבלות", "אחר"]

def get_tag(text, tag_list):
    model_name = 'gemini-1.5-flash'  # Replace with an available model name if needed
    model = genai.GenerativeModel(model_name)
    genai.configure(api_key='AIzaSyB3h0w_rzHYiaFDP6PJ5VqiBw3l8sKF3hA')

    # Define your tag lists
    tag_list_activity = ["תעסוקה", "מוביליות חברתית", "חינוך והשכלה", "בריאות נפשית", "בריאות", "אחר", "קהילה"]
    tag_list_population = ["החברה הערבית", "החברה החרדית", 'קהילת הלהט"ב', "קהילת יוצאי אתיופיה",
                           "אוכלוסיות בסיכון ומצבי קצה", "אנשים עם מוגבלות", "אחר"]

    try:
        # Ensure there's a delay of 7 seconds before making the request
        time.sleep(3)

        prompt = f"Given the next Hebrew text: '{text}', which of these tags is the best match? in case there is 2 which likeley, return more than 1 {tag_list}. Return only the tag/s and nothing else. "
        response = model.generate_content(prompt)

        return response.candidates[0].content.parts[0].text
    except RequestLimitExceededError:
        end_time = time.time()
        return "Error: The request limit has been exceeded. Please try again in few minutes."
    except Exception as e:
        return f"An error occurred: {str(e)}"
#
#
# text_example = (""
#                 "בני נוער ממוסדות טיפול חוץ בגילאים 15-18. בני נוער הנתקלים במשבר ספציפי ומזוהים על ידי מקצוענים ככוחות רפואיים לשיקום - נקראים בני הסערה. בני נוער שבהם המוסד מאמין ביכולותיהם, בפרופיל שלהם ובתאימותם לפעילויות המוסד שיאפשרו להם להשלים את התהליך אצלם, בתמיכה במשבר הספציפי הנוכחי, נתונים מדווח השנתי של הרשות האחראית על בתי המשפט מציינים כי 10 אחוזים מהאוכלוסייה נמצאים בסכסוך בכל שנה, מה שמציין כי הקהל היעד הכולל חורג על פי 800,000 איש בשנה רק בישראל בלבד. בנוסף, הדוח מדגיש על חוסר העמיסה והזמן המשמעותי שנדרש לעיבוד. אנו מציגים מספר נקודות דגש נגישות ראשיות של התהליך בכל מקום ובכל זמן, יצירת תעסוקה לאנשים שיצאו מהשוק התעסוקתי ויכולים לחזור, משתתפים בצורה פעילה בתהליך ותורמים להם ולחברה, פתרון הסכסוכים בין מוסדות טיפול חוץ: פתרון הסכסוכים ופתרון קונפליקטים.")
text_example= "הארגון מתמקד בקידום שוויון והשוויון בחברה ובקידום הזכויות של אנשי האוכלוסיה הגאה. דרך מגוון פעילויות ותוכניות, אנו מבצעים פרויקטים המיועדים לשפר את המציאות של אנשי הקהילה, ולתת מענה לצרכיהם הייחודיים. במסגרת פעילותנו, אנו מקדמים דיאלוג והבנה בין אנשים מקהילות שונות, על מנת לייצר סביבה חברתית פתוחה ומקבלת, ולהפחית את הפערים החברתיים והתרבותיים בין האנשים בחברה."


print(f"from tag_list_age:"+get_tag(text_example, tag_list_age))
print(f"from tag_list_activity:"+get_tag(text_example, tag_list_activity))
print(f"from tag_list_population:"+get_tag(text_example, tag_list_population))

tag_list_age = ["הגיל הרך", "ילדים ונוער", "צעירים", "הזדקנות מיטבית, אנשים מעל גיל 90", "אחר"]


def get_tags_activity(df, result_df=None):
    global progress
    results = []
    model_name = 'gemini-1.5-flash'  # Replace with an available model name if needed
    model = genai.GenerativeModel(model_name)
    genai.configure(api_key='AIzaSyB3h0w_rzHYiaFDP6PJ5VqiBw3l8sKF3hA')
    tag_list = ["תעסוקה", "מוביליות חברתית", "חינוך והשכלה", "בריאות נפשית", "בריאות", "אחר", "קהילה"]

    for i in range(len(df)):
        text = str(df.iloc[i, 10])
        print(text)
        prompt = f"Given the next Hebrew text: '{text}', which of these tags is the best match?  {tag_list}. Return only the tag/s and nothing else. "
        response = model.generate_content(prompt)
        results.append(response)

        # Update progress
    newname = "תג -  תחום חברתי"
    new_column_df = pd.DataFrame(results, columns=[newname])

    if result_df is None:
        result_df = pd.DataFrame(index=df.index)

    result_df = result_df.join(new_column_df)
    return result_df


def get_tags_age(df, result_df=None):
    global progress
    results = []
    model_name = 'gemini-1.5-flash'  # Replace with an available model name if needed
    model = genai.GenerativeModel(model_name)
    genai.configure(api_key='AIzaSyB3h0w_rzHYiaFDP6PJ5VqiBw3l8sKF3hA')
    tag_list = ["הגיל הרך", "ילדים ונוער", "צעירים", "הזדקנות מיטבית, אנשים מעל גיל 90", "אחר"]

    for i in range(len(df)):
        text = str(df.iloc[i, 10])
        print(text)
        prompt = f"Given the next Hebrew text: '{text}', which of these tags is the best match?  {tag_list}. Return only the tag/s and nothing else. "
        response = model.generate_content(prompt)
        results.append(response)

        # Update progress
    newname = "תג -  תחום חברתי"
    new_column_df = pd.DataFrame(results, columns=[newname])

    if result_df is None:
        result_df = pd.DataFrame(index=df.index)

    result_df = result_df.join(new_column_df)
    return result_df


def get_tags_population(df, result_df=None):
    global progress
    results = []
    model_name = 'gemini-1.5-flash'  # Replace with an available model name if needed
    model = genai.GenerativeModel(model_name)
    genai.configure(api_key='AIzaSyB3h0w_rzHYiaFDP6PJ5VqiBw3l8sKF3hA')
    tag_list = ["החברה הערבית", "החברה החרדית", 'קהילת הלהט"ב', "קהילת יוצאי אתיופיה",
                           "אוכלוסיות בסיכון ומצבי קצה", "אנשים עם מוגבלות", "אחר"]
    for i in range(len(df)):
        text = str(df.iloc[i, 10])
        print(text)
        prompt = f"Given the next Hebrew text: '{text}', which of these tags is the best match?  {tag_list}. Return only the tag/s and nothing else. "
        response = model.generate_content(prompt)
        results.append(response)

        # Update progress
    newname = "תג -  תחום חברתי"
    new_column_df = pd.DataFrame(results, columns=[newname])

    if result_df is None:
        result_df = pd.DataFrame(index=df.index)

    result_df = result_df.join(new_column_df)
    return result_df



