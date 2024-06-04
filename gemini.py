
import google.generativeai as genai

def gemini(prompt, text):
    model_name = 'gemini-1.5-pro-latest'  # Replace with an available model name if needed
    model = genai.GenerativeModel(model_name)
    genai.configure(api_key='AIzaSyB3h0w_rzHYiaFDP6PJ5VqiBw3l8sKF3hA')
    combined =  prompt + text
    response = model.generate_content(combined)
    text = response.candidates[0].content.parts[0].text
    return (text)

prompt = "take the next Hebrew and shorten this passage to up to 2 sentences in hebrew, return only the shorten text "
prompt2 = "take the next Hebrew and rewrite the passage in hebrew, return only the shorten text "
hebrew_text = "נערים ממסגרות חוץ ביתיות בגילאי 15-18.\n ערים המצויים במשבר נקודתי ומסומנים ע\"י אנשי המקצוע כפוטנציאל נשירה- נערים ב'סערה'.\nנערים אשר המסגרת מאמינה בכוחות, בפרופיל ובהתאמה לפעילות המסגרת ככאלו שיאפשרו לו לסיים את התהליך אצלם, בהינתן התמיכה במשבר הספציפי הנוכחי."
print( gemini(prompt, hebrew_text))
print( gemini(prompt2, hebrew_text))