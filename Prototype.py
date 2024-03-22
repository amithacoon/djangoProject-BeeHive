import pandas as pd
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
# Set your OpenAI API key here
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define your tag lists
tag_list_activity = ["תעסוקה", "מוביליות חברתית", "חינוך והשכלה", "בריאות נפשית", "בריאות"]
tag_list_age = ["הגיל הרך", "ילדים ונוער", "צעירים", "הזדקנות מיטבית"]
tag_list_population = ["החברה הערבית", "החברה החרדית", 'קהילת הלהט"ב', "קהילת יוצאי אתיופיה", "אוכלוסיות בסיכון ומצבי קצה", "אנשים עם מוגבלות"]
# File path
input_csv_path = 'path/to/your/input.csv'
output_csv_path = 'path/to/your/output.csv'

# Load the CSV data into a DataFrame
df = pd.read_csv(input_csv_path, encoding='utf-8')

# Function to query OpenAI and get tag
def get_tag(text, tag_list):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Given the text: '{text}', which of these tags is the best match? {tag_list}",
        temperature=0.3,
        max_tokens=60
    )
    return response.choices[0].text.strip()

# Iterate over rows in DataFrame and get tags
for index, row in df.iterrows():
    df.at[index, 'תחום פעילות Tag'] = get_tag(row['תחום פעילות'], tag_list_activity)
    df.at[index, 'קהל יעד- גיל Tag'] = get_tag(row['קהל יעד- גיל'], tag_list_age)
    df.at[index, 'קהל יעד - קבוצות אוכלוסייה Tag'] = get_tag(row['קהל יעד - קבוצות אוכלוסייה'], tag_list_population)

# Save the modified DataFrame to a new CSV file
df.to_csv(output_csv_path, index=False, encoding='utf-8')

print("Processing complete. The output file has been saved.")
