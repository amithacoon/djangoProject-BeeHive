from django.shortcuts import render

from django.shortcuts import render

def home(request):
    rows = [
        {'col1': 'דוגמה 1',
         'col2': 'נערים ממסגרות חוץ ביתיות בגילאי 15-18 .\nנערים המצויים במשבר נקודתי ומסומנים ע"י אנשי המקצוע כפוטנציאל נשירה- נערים ב\'סערה\'.\nנערים אשר המסגרת מאמינה בכוחות, בפרופיל ובהתאמה לפעילות המסגרת ככאלו שיאפשרו לו לסיים את התהליך אצלם, בהינתן התמיכה במשבר הספציפי הנוכחי.',
         'col3': 'נשירה בקרב מסגרות חוץ ביתיות',
         'col4': 'מרחב חווה חקלאית בסביבה מדברית מנותקת, בו הנער שוהה בשילוב עם עבודה חקלאית ועבודת חיות משק בתצורה יומיומית ולימדת יישום של מיומנויות שדאות מדבריות בתוך סביבה חינוכית-טיפולית עוטפת למשך תקופה של 8 שלבים המוערכים בכשלושה חודשים.',
         'col5': 'כן',
         'col6': "התנדבתי ופעלתי במסגרות שונות. בשנת 2015 ייסדתי את 'עמותת ניצן לזכרם' ומאז אני עוסק בפעילות זו.",
         'col7': 'כן', 'col8': 'הקמת עמותה, כתיבת תכנית עסקית, תכנית טיפולית, והקמת חוות נוער טיפולית',
         'col9': "לצערנו אין מתחרים. אין כיום מסגרת לטיפול בנוער נושר ממסגרות חוץ ביתיות במדינת ישראל. יש מס' מענים מצומצמים שמסגרות ספציפיות פתחו לצרכים פנים מסגרתיים. אך אין גוף שנותן מענה רחב היקף למסגרות שונות. ",
         'col10': "למעשה, אנו המסגרת היחידה שנותנת מענה רחב למסגרות חוץ ביתיות. לרוב המסגרות החוץ ביתיות אין מענים להתמודדות עם נערים ב'סערה' לפני שהם נושרים."},

        {'col1': 'דוגמה 2',
         'col2': 'קהל היעד של המיזם כולל שני מעגלים:\n1. צעירים בגילאי 18-35 המתמודדים עם משבר נפשי, אשר מוביל לפגיעה בתפקוד עד כדי הימנעות ממעגלי החיים והסתגרות בבית. \n2. בני משפחותיהם של הצעירים.\n\nבהתבסס על הצלבות נתונים של משרד הבריאות והלמ"ס, בישראל חיים עשרות אלפי צעירים שמתמודדים עם בעיות נפשיות שמובילות לפגיעה משמעותית בתפקוד. חלקם מאובחנים במצבים של דיכאון קליני, חרדה מוכללת, סכיזופרניה, מצבי פסיכוזה, הפרעה טורדנית כפייתית. חלקם אינם מאובחנים כלל. אלה שמאובחנים - לאו דווקא מוכרים (למשל מאובחנים על ידי פסיכיאטר פרטי או פסיכולוג קליני, ולא במערכת ציבורית). חלקם מאובחנים ומוכרים, ועדיין לא מצליחים להיעזר במערכות התמיכה הקיימות, כמו למשל סל שיקום.\n\nבמצבים משבריים ממושכים של צעירים, התא המשפחתי כולו מושפע מכך עמוקות. על פי הספרות המחקרית מעורבות המשפחה בתהליכי טיפול ושיקום היא קריטית ליכולת של הצעיר.ה להשתקם, להחלים ולשוב להשתתפות תפקודית במעגלי החיים. נוסף על כך, גם המשפחה זקוקה לרשת תמיכה מקצועית.',
         'col3': 'היעדר שירותים ייעודיים למשברים נפשיים אקוטיים בקהילה. המענה המרכזי, וכמעט היחידי, לטיפול במצבי משבר פסיכיאטריים אקוטיים הוא חדר המיון ומחלקות בבית החולים הפסיכיאטרי. במדינות מפותחות קיים מגוון עשיר של מנגנוני התערבות במצבי משבר שכאלה.\n\nהמענה המצומצם מוביל למצוקה רבה אצל המתמודדים עם משברים נפשיים אקוטיים ואצל בני משפחותיהם, ומונע טיפול מיטבי וניצול נכון של המשאבים העומדים לרשות מערכת בריאות הנפש. קיימת היענות נמוכה לטיפול משום שהוא יכול להוביל להגעה למיון פסיכיאטרי. נפגעי הנפש ובני משפחותיהם חוששים מכך בעקבות הסטיגמה המלווה, קישור אוטומטי בין מיון ואשפוז, הערכה (נכונה או שגויה) שלפיה חומרת המצב אינה מצדיקה אשפוז, פחד מפני אשפוז בכפייה וטראומטיזציה על רקע חוויית אשפוזים קודמים.\n\nנוסף על כך, 53% מהאנשים המאושפזים לראשונה, יתאשפזו בשנית. יש צורך דחוף ובוער במענה מקצועי איכותי, מקיף ואפקטיבי, המאפשר למנוע אשפוזים לא נחוצים, תוך יצירת רשת תמיכה משפחתית, ומעל הכול - יצירת הזדמנות לשיקום בר קיימא, המאפשר השתלבות חברתית ויצרנית של הצעירים.\n\n* תיאור המציאות המובא כאן מבוסס על דו"ח של המועצה הלאומית לבריאות הנפש שיצא ביולי 2019.',
         'col4': 'הגעה של איש או אשת מקצוע מתחום בריאות הנפש לבית המשפחה, כחלק מתהליך התערבות ייעודי ומובנה. צוות "הקול שבפנים" הינו רב-מקצועי וכולל דיסציפלינות שונות מתחומים של עבודה סוציאלית קלינית, טיפול משפחתי, ריפוי בעיסוק, פסיכותרפיה, פסיכולוגיה קלינית, גישת ההתנגדות הלא-אלימה, ובהמשך – דיאלוג פתוח. הסטינג כולל מפגשים בני שעה עד שעה וחצי, המתקיימים בין פעם לשלוש פעמים בשבוע לאורך שלושה חודשים עד שנה. המפגשים הינם משפחתיים ופרטניים באופן המותאם לצרכים – ישנם מספר מסלולי ליווי מוגדרים. תהליך ההתערבות נשען בין היתר על הגישה המערכתית, שרואה את המשבר האישי בהקשרים רחבים – משפחתיים, חברתיים וקהילתיים, והוא עוזר בכך שמאפשר רכישת ידע על אודות המצב המשברי של הצעיר; ונטילציה לתחושות קשות; העמקה בדינמיקה המשפחתית; פירוק סטיגמה של בני משפחה וסטיגמה עצמית; סיוע לכל מי שמתמודד עם קשיים במשפחה; גיבוש שפה משותפת; יצירת סדר והרגעה; הצבת גבולות ויצירת נפרדות; שיפור התפקוד ובניית עצמאות; קשר ותיאום עם גורמי טיפול ושיקום – פסיכיאטר, סל שיקום ועוד; הפנייה לשירותים נוספים בקהילה ומניעת אשפוזים לא נחוצים באמצעות מעטפת תמיכה וניהול של המשבר הנפשי.',
         'col5': 'כן',
         'col6': 'אני (אוריה) בוגר תכנית "שגרירי רוטשילד", שמטרתה לקדם את החברה בישראל תוך יצירת רשת מנהיגות חברתית. השתתפתי בתכנית במהלך שנות לימודי וצברתי ניסיון מעשי בפיתוח וניהול של מיזמים קהילתיים, כמו למשל הקמה ותפעול של ליגת קטרגל לבני נוער, שבה יש דגש על גיבוש חברתי וערכים.\n\nלפני שהקמתי את הקול שבפנים, עבדתי בחברת אשנב כמנהל שיווק. פעילות החברה מתמקדת במתן מענים מתקדמים לאנשים עם מוגבלות, לרבות צעירים מתמודדי נפש במסגרת סל שיקום של משרד הבריאות.\n\nעופר - מנכ"ל עמותת "שכולו טוב", המובילה פתרונות שילוב חדשניים בתחום התעסוקה למתמודדי נפש.\n\nחשוב להדגיש כי אין קשר בין פעילות עמותת "שכולו לטוב" ל"קול שבפנים".\nארגון "הקול שבפנים" הינו עסק חברתי בבעלות משותפת של אוריה, עופר ועירד.',
         'col7': 'כן',
         'col8': 'אוריה - "..." התחיל כיוזמה עצמאית שלי ב-2016.\n\nעירד - הקים את עמותת "..." ואת הפלטפורמה הדיגיטלית ..., שבה בני נוער משתתפים בקבוצות תמיכה חברתיות מקוונות.',
         'col9': 'Outreach -  טיפול פסיכולוגי שמגיע עד אליך\nדיאלוגיה - טיפול ביתי ממשבר להחלמה\nמרכז מרחבים - מומחים לטיפול פסיכולוגי (לרבות טיפולי בית)',
         'col10': '1. מיקוד בקהל יעד של צעירים תוך התמחות הולכת וגדלה.\n\n2. גמישות במענה המקצועי הכוללת מספר מסלולי ליווי שמצד אחד מוגדרים, ומצד שני ניתנים להתאמה אישית תוך חשיבה משותפת עם המשפחה - קבלת החלטות משותפת היא לתפיסתנו המקצועית מודלינג מרכזי ומהותי עבור התא המשפחתי, שמאפשר אימפקט מהרגעים הראשונים של ההתערבות.\n\n3. הנגשת השירות ברמה מקצועית וכלכלית על ידי אפשרות לקיום פגישה אחת בשבוע (חלק מהמתחרים שלנו מחזיקים בגישה שאי אפשר להיכנס להתערבות במצבי משבר מהסוג הנ"ל, אם אין התחייבות מראש על 3 מפגשים בשבוע, מה שלתפיסתנו יכול למנוע ממשפחות להיכנס לתהליך ולהיעזר).\n\n4. צוות מקצועי צעיר (נע סביב גילאי 30-35).\n\n5. יצירת ערך תמידי - אנחנו לא מעוניינים רק בלקוחות משלמים. אלא ביצירת קהילה ובמתן ערך בכל אינטראקציה. לכן, בכל פנייה אלינו, גם אם אנו לא הכתובת המקצועית, אנו מקפידים לתת את כל המידע שיש לנו ולסייע ולהכווין באופן פרואקטיבי למיצוי זכויות, שהינו לוקה מאוד בחסר בקרב קהל היעד שלנו.'},
        {'col1': 'דוגמה 3',
         'col2': 'מנתוני הדוח השנתי של הממונה על בתי המשפט עולה ש 10 אחוז מהאוכלוסייה נמצאים בכל שנה בסכסוך מכאן שקהל היעד הכולל עולה על 800 אלף איש בשנה רק בארץ. בנוסף ניתן ללמוד מהדוח על מצוקת העומס וכן על הזמן הרב שהולך לעיבוד. אנו מביאים מספר בשורות ראשית הנגשה של התהליך לכל מקום ובכל זמן ,יצירת תעסוקה לאנשים אשר יצאו ממעגל העבודה יכולים לחזור ולקחת חלק פעיל התורם להם ולחברה',
         'col3': 'ישוב סכסוכים ופתרון קונפליקטים',
         'col4': 'לפתרון שלנו שני צדדים . צד אחד פונה לצדדים ומאפשר להם להעלות את טענותיהם .\nהצד השני פונה לקהילה של וויזרים המחוברת עם כלי הניהול שלנו אשר מאגד את החלטתם. \nהתהליך שיצרנו יוצר שקיפות ואמינות גבוהה המביא איתו אמון רב בתהליך ובהחלטתה',
         'col5': 'כן', 'col6': 'הייתי חלק מהאב הראשון בתל אביב', 'col7': 'כן',
         'col8': 'אופיר יזם סידרתי ושותף בפא... מעבדה לפיתוח ספורטק\nנוי יזם בתחום המו"מ והגישור ממובילי התחום בארץ ',
         'col9': 'חברות ADR/ODR',
         'col10': 'היתרון התחרותי שלנו חיסכון בזמן וכסף גם לצדדים וגם למערכת .פיתחנו על בסיס ניסיונו כלי חדש אשר משלב בין הצורך של אנשים לביטחון בתהליך לבין היכולת הקיימת לבנות איזונים כך שהחוויה של הצדדים ושל הוויזרים (השופטים) תהיה של הליך הוגן ואמיתי וזאת בניגוד למתחרים אשר בחרו בדרך הקלה ולקחו את הכלי הקיימים והעלו אותם לרשת'},
        {'col1': 'דוגמה 4',
         'col2': 'תלמידים בסכנת נשירה ותלמידים שלא צפויים לסיים עם תעודת בגרות מלאה ו או 12 שנות לימוד',
         'col3': "החל מאמצע כיתה ט' היקף הנשירה הסמוייה והרשמית ממערכת החינוך גדלה. \nהתוכנית נותנת מענה  לתלמידים בנשירה ולתלמידים שלא יסיימו עם תעודת בגרות בגלל התנהגות והרגלים המאפיינים נוער בסיכון",
         'col4': 'מודל הפעולה של האירגון כולל ליווי פדגוגי תלת שנתי של המורים המלמדים בכיתות אומץ ואתגר לשיטת לימוד מבוססת מקום של הנושאים בהסטוריה תנך אזרחות ספרות ואנגלית מתוך תכנית הלימודים לבגרות.\nבנוסף בכל שנה בתיכון יתקיימו 3 מסעות שטח ארוכים בניהול עצמי של התלמידים בהם המורים ישלימו את ההוראה מבוססת המקום לתלמידיהם. (המורים המקצועיים מגיעים להוראה חד יומית בנקודות הרלונטיות ולא נדרשים לצאת למסע מלא) \nמסעות השטח אורכים 10 ימים כל אחד בניהול עצמי של התלמידים והם מסעות טיפוליים בשיטת Wilderness therapy ומלווים על ידי אנשי מקצוע. מטרתם להעלות מוטיבציה ולמטב הרגלים של אחריות, התמדה, נתינה, מיקוד שליטה פנימי, יוזמה, שיתופיות, נתינה ועוד',
         'col5': 'כן', 'col6': 'נסיון מועט כמתנדבת בארגונים חברתיים ', 'col7': 'לא', 'col8': '',
         'col9': 'דרך לוטן ונירים בשכונות הם באותו תחום אבל לא מהווים תחרות ממש מ 4 סיבות:\n1. הם מציעים רק את הציר של עיצוב התנהגות ולא את הפדגוגיה.\n2. הם מציעים ארוע נקודתי ומסע של ימים ספורים בלבד ולא תהליך מתמשך של 3 שנים. מבחינת הנער ההשפעה של המסע הבודד שעבר היא נקודתית ולא מתמשכת.\n3. מחיר- העלות של המסעות שלהם כפולה משלי. אצלי המנגנון מאוד רזה אין תקורות לכל מיני חברות ומנהלים ומנהלי מנהלים',
         'col10': 'זה הארגון היחידי בארץ ואולי גם בעולם שמשלב פורמאלי עם בלתי פורמאלי. שמשלב למידה של חומר עיוני לבגרות עם חינוך. אף אחד לא עושה זאת. ובטוח שלא בתיכון. כל המיזמים החדשניים בחינוך נגמרים בסוף היסודי או גג בחט"ב. בחטיבה עליונה כולם מתיישרים בהוראה פרונטאלית ומסורתית לקראת בחינות הבגרות אין שום חדשנות. \nיתרון תחרותי נוסף הוא הליווי הפדגוגי של המורים- המורים עצמם עושים שינוי שמשפיע על כל בית הספר. \nיש פיילוט עובד ומוכך עם מספרים \n'},
        {'col1': 'דוגמה 5',
         'col2': 'קהל יעד מגוון - פלטפורמה המאפשרת לכל אחד ולמערכת לקבל הבנה טובה יותר בין מה שהוא אוהב, טוב בו ויכול להתפרנס ממנו ושהעולם צריך...',
         'col3': 'מיזם טבלת הסמלים האינטראקטיבית של טינג\nהבעיה היא שהרבה תלמידים ומורים לא ממש יודעים איזה מקצועות קיימים כיום, במקרה הטוב, תלמידים מסיימים תיכון כשהם מכירים רק את המקצוע של ההורים.  \nאם תלמידים לא יודעים אילו מקצועות יש היום, איך הם ידעו אלו מקצועות יהיו מחר כאשר קצב הטכנולוגיות חוד חנית מתקדם כל כך מהר? \nובכלל - מה אני רוצה להיות? \n',
         'col4': 'הצורך הוא בארגז כלים ללמידה והבנה של אילו מקצועות יש והכנה למקצועות העתיד כך שכל אחד ואחת יוכלו להתעסק בדברים שמעניינים אותם ויותר מזה, שמתחברים ל 17 מטרות פיתוח בר קיימא שהצבנו לעצמנו.\nהפתרון -  טבלת הסמלים של טינג – המנגישה/החושפת אותנו למה שקיים ומאפשרת לנו ליצור את מקצועות העתיד בהתאמה מלאה למטרות פיתוח בר-קיימא. כי חדשנות מתרחשת בהתאם לכאבים אמיתיים.\nהמסר שלי אליכם -  תכינו את התלמידים שלכם לעתיד שהוא כבר פה.',
         'col5': 'כן',
         'col6': '2005 – היום     עצמאי - יועץ בנושאי חדשנות, קיימות ויצירתיות. \nיועץ ומפתח תכני לימוד בעברית, אנגלית וסינית.\n\tמתמחה בניהול וליווי של קהילות. בין היתר עבדתי בישראל עם ארגונים ומוסדות כמו מש"ב (יחידת החינוך של משרד-החוץ) הטכניון, אונ\' בן-גוריון, משרד החינוך ואחרים, נכון להיום שיטת טינג לחשיבה יצירתית רב-תחומית שפיתחתי הגיעה ליותר מ - 50 מדינות וקהילות וקבוצות שייסדתי במדיה החברתית הגיעו לאלפים ועשרות אלפי חברים. \nבחו"ל בין היתר עבדתי עם ארגונים כמו,  HKEJ, Presente, SheLovesTech , SmileForTaiwan, Asia Trend,\n\n2019 \t\tיועץ פיתוח והקמה קהילת SDGI ישראל\n',
         'col7': 'כן',
         'col8': 'בשנתיים האחרונות אני יוצר ומקדם שיטת חשיבה שפיתחתי ותכנים חינוכיים וחדשניים כחלק ממיזם בינלאומי הידוע בשם \'..\' – לחדש בדרך משחק. חלק נכבד מהתכנים משותפים ברשת ובאתר של משרד החינוך באופן חופשי לטובת הכלל מתוך מטרה לחבר, להתחבר ולהעניק השראה לעולם החינוך. המטרה של המיזם היא לקדם שיח סביב מציאת פתרונות לאתגרי האנושות SDG (Sustainable Development Goals), כפי שהוגדרו על ידי האו"ם. הסדנאות של טינג הועברו לאנשי חינוך ביותר מחמישים מדינות, בבתי הספר, באקדמיה ובתוכניות שותפות של האו"ם וכיום היא מומלצת ונתמכת ע"י משרד החינוך. ',
         'col9': 'SIT ',
         'col10': 'פתרון מערכתי הכולל מתן פתרון בתחום החינוך בזמן שכל המתחרים הם בשוק העסקי. כן, בהקשר של שותפים פוטנציאלים, יזמים צעירים, יוצרים שינוי, יוניסטרים, משרד חינוך ואחר, המערכת הדיגטלית שלנו עוזרת להם ליצירה , ניהול ושיתוף של רעיונות ברמת המערכת וככלל מיפוי של שוק העבודה העתידי. '},
        {'col1': 'דוגמה 6', 'col2': 'לימוד אסטרטגיות וניהול עצמי במצבים משבריים',
         'col3': 'תגובות לא מיטביות במצבים משבריים',
         'col4': 'תוכנית הכשרה למדריכים - ניהול עצמי לנערות ונערים במצבי משבר בעזרת פרוטוקולים גופניים', 'col5': 'כן',
         'col6': 'לימדנו פיילוט של השיטה במשך סמסטר בביה״ס התיכון עמל בלוד ובמשך שנה בבית הספר התיכון עירוני ה׳ בתל אביב  ',
         'col7': 'לא', 'col8': '', 'col9': 'אנחנו לא מכירים סדנה דומה',
         'col10': 'יש לנו סדנה שעברה סטנדרטיזציה ונסיון רב בהכשרת מדריכים'},
        {'col1': 'דוגמה 7',
         'col2': 'האוכלוסיה של המועסקים במיזם תהיה של אזרחים ותיקים הנמצאים במצב כלכלי קשה החיים בפריפריה שבבקעת הירדן ואינם יכולים למצוא תעסוקה. בנוסף תשתלבנה בנות אולפנה כחלק מלימודי טכנולוגיה שלהן.',
         'col3': 'תעסוקה למבוגרים, פרנסה מכובדת בשילוב השכלה טכנולוגית לבנות נוער דתיות - כל זה קורה בפריפריה במקום בעל מעט אמצעים כלכליים',
         'col4': 'אזרחים ותיקים ונערות אולפנה ירכיבו את המוצר . בשילוב הזה אטפל בבעיית בדידותם של הוותיקים וגם קושי בפרנסה . נערות האולפנה יזכו בחינוך טכנולוגי וכן יזכו בשיעור באזרחות טובה',
         'col5': 'כן',
         'col6': 'מנהלת קהילה וקליטה בשנתיים האחרונות במושב חמרה. מתנדבת בעמותת "עלם" בתוכנית "דרך המלך", מגשרת מתנדבת בבית משפט השלום בעכו וכן במרכז האוניברסיטאי תל-אביב',
         'col7': 'כן', 'col8': 'שותפה בהקמת פורום נשות עסקים בפתח תקווה.', 'col9': 'kitos',
         'col10': 'המוצר מיועד לציבור הדתי , ערכות למידה טכנולוגיות בהנגשה לציבור זה עם אלמנטים דתיים, מפעל שומר שבת.'},
        {'col1': 'דוגמה 8',
         'col2': 'אוכלוסיית תל אביב המעוניינת לקחת חלק בעשייה סביבתית-חברתית במרחב האורבני תחילה ומחוצה לו בהמשך. אנשים שרוצים להיות פעילים ברמות השונות אך לא מוצאים את ערוץ נגיד, המדבר בשפה שלהם, שיכול להציע עשייה ברמה גבוהה וגם מינימלית כחלק מחי היום יום, כאלו שיש להם פער של ידע בתחום.',
         'col3': 'אנחנו רוצים להשפיע על המודעות והמציאות בתל אביב. לייצר ולתמוך ביוזמות סביביתיות-חברתיות. להשפיע על התרבות הצרכנית בעיר. לעורר את המעורבות של אלו שלאחרונה החלו לעסוק במשב הסביבתי. מהעסקים, למשרדים, לאומנות, לאופנה, למוצרים, למוסיקה, לשפה והחינוך. ',
         'col4': 'תחילה, מודל הפעולה שלנו מחולק ל 3 מחלקות:\n1. תוכן דיגיטלי ממוקד לחיי היום יום. \nמנגישים מידע רלוונטי לאורח חיים אקולוגי, פתרונות עירוניים, ניתן רוח גבית לכל פרויקט ומיזם ברוח אקולוגית.\n2. עולם התרבות: אירועים, תערוכות, כנסים, מסיבות ירוקות ברוח אקולוגית ועוד.\n3. עבודה מול עסקים \nכעת אנו עובדים על מיפוי מקיף של הסטטוס האקולוגי של כלל העסקים בתל אביב, כדי לתת תמונה מדוייקת של המצב האקולוגי שלהם/שלנו. \nלעסקים שירצו "להתיירק" אנחו מציעים פתרונות מגוונים: חיבור לספקים, פתרונות קונספטואליים, שיווק, רוח גבית, קהילה, שתפ"ים ועוד.\n\nבעתיד - החזון שלנו הוא להיות "חממה" אשר מייצרת ותומכת בפרוייקטים סביביתיים-חברתיים במרחב האורבי.\n',
         'col5': 'לא', 'col6': '', 'col7': 'כן',
         'col8': 'ליווי בפיתוח מספר עסקים ויוזמות, מעסק תבחום המזון, למיזם אדריכלי לבניית בניין ה"מכיל" את עצמו (אנרגיה מתחדשת, ביו גז, חות גג, וכו...) ועוד...',
         'col9': 'לא מצאנו מתחרים ישירים. וזו הסיבה שבחרנו להקים את המיזם מאחר וראינו את הצורך של הקהילה שלנו ולא מצאנו מענה.\nאולי Save-it. שאיתם אנחנו בקשר טוב מאוד, משתפים פעולה וידע.',
         'col10': 'קהל היעד, זהו קהל יעד שלא מצאנו עוד מיזם ברוח הזו השאוף להתמקד בקהל יעד הזה.'},
        {'col1': 'דוגמה 9',
         'col2': '\nאנחנו עובדים עם שורדות סחר ובבני אדם ונפגעות זנות בישראל. חלקן מוכרות על ידי ביטוח לאומי חלקן לא.\n',
         'col3': 'אנחנו עוסקים בשני בעיות, אחת היא תעסוקה ושיקום לנשים וגברים שרוצים לצאת ממעגל הזנות אך אין להן משגרת בטוחה ותומכת אשר מספקת להם עבודה בתנאים הוגנים ומעטפת של תמיכה והעצמה. 76% מהנשים בזנות רוצות לצאת אבל לא יודעת איך או לאן, רובן בלי הכשרה ועם פגיעות נפשיות. אנחנו מספקים להם הכשרה ותעסוקה הוגנת, ארוכת טווח ותמיכה פסיכוסוציאלית. \nהבעיה השנייה היא בעיית זבל ומחזור, בארץ יש עשרות אלפי קייטים (עפיפוני ים) מצנחים, מפרשים וחליפות גלישה שנזרקות לאחר מספר שנים מועט בלי שום תהליך של מחזור מדובר במאות אלפי מטרים רבועים של חומר עמיד  אשר לא מתכלה ונזרק לזבל.  אנחנו ממחזרים את החומרים  מהקהילה בארץ\n',
         'col4': 'אנחנו מספקים תעסוקה שיקומית והעצמה, כיום ממחזרים מעל 10,000 מטר ריבוים של חומר בשנה, מספקים  מעל 10,000 שעות של תעסוקה שיקומית בשנה ובונים מודלים חדשים על מנת להגדיל את ההכנסה על מנת להגדיל ולשכפל את המודל בעוד מקומות. הנשים שבאות לעבוד אצלנו מגיעות לתקופה של שנה ויותר (בהתאם לרצון שלהן)',
         'col5': 'כן',
         'col6': 'אני אישית, הקמתי יוזמי חברתית עסקית של שוק אוכל מקומי  בשיתוף עיריית תל אביב יפו בשם תוצרת יפו בשנת 2015 \nhttps://www.haaretz.co.il/food/food-news/1.2774610\nניהלתי שנה פרויקט של פיתוח קהילתי בגאנה בתחומי חינוך, בריאות וחקלאות. \nניהלתי שנה פרויקטים רחבים וגדולים של IsraAID ביוון, בתחומים של רפואה, תמיכה פסיכוסוציאלית, אינטגרציה, העצמה וחינוך לפליטים. \n\n\n\n\n\n ',
         'col7': 'כן',
         'col8': 'בשנת 2015 הקמתי יוזמה של שוק אוכל מקומי בשיתוף עיריית תל אביב יפו, \nהקמתי שותפויות ופרויקטים בגאנה עם ראשי קהילה, בתי ספר ומשרד הבריאות.\nביוון  גיסתי כספים והקמתי פרויקט אינטגרציה ייחודי במאות אלפי דולרים אשר ממשיך עד היום ומאד מצליח.   \n\n\n',
         'col9': 'בארץ זה מותגים כמו Kankan ובחו"ל FREITAG אין אך מיזם שפועל כמונו בארץ שמייצר כאן.',
         'col10': 'ברמה החברתית הוא עובד על פתרון בעיות חברתיות וסביבתיות  לוקליות אין עוד מיזם שעושה את מה שאנחנו עושים עם האימפקט שיש לנו, קרי תעשוקה לאורך זמן עם שכר הוגן בסביבה מוגנת ומעצימה.  \nברמת המוצר הוא ייחודיי (one of a kind) עם שקיפות מלאה לגבי איפה וממה הוא נוצר, אופנתי ומאד עמיד.\n\n  '},
        {'col1': 'דוגמה 10',
         'col2': 'Social skills are the tools that enable children to communicate, make friends and develop healthy relationships. Those skills are learned and composed of specific behaviors. Evidence shows that there is an increase in the incidence of children with social difficulties. Studies indicate that 26% of children suffered from social rejection at school. The implications of Social Skills Deficit are: Decrease in academic achievements, Emotional Distress, Low self-esteem and In extreme cases, bullying and social rejection and isolation can lead to suicide. we address children with social difficulties on a variety of backgrounds: attention difficulties, emotional difficulties, learning disabilities.',
         'col3': 'The effective intervention for social skills deficits is group therapy, but setting the right groups is a tedious and expensive process, and not all children can handle face to face simulations because of a high level of anxiety. On the other hand, at individual therapy – the setting is easier but the efficiency is unclear. there is also a lack of resources and professionals in the public sectors. Solutions are accessible to 1:9 kids.',
         'col4': 'we provide an innovative certified Social Skills Trainer, using VR technology. The system is based on CBT Social Skills Training protocols, it contains 10 interactive sessions (guided by a coacher avatar), each session focused on different social skill, and involves the use of avatars in a classroom and school courtyard visual environment.\nNext prototype new capabilities:  Data acquisition during the session, kids performance assessment algorithms, AI engine for changing session content dynamically. This unique database will enable researchers to generate better CBT protocols and improve performance by personalizing education.          \n',
         'col5': 'כן',
         'col6': 'I worked on the project “Hadarim hamim” – Schmidt program - in psychological treatments at schools for children at risk, And with the welfare department in Beer Yaakov and Ramla in psychological treatments for children and teens who have been victims of sexual assault.',
         'col7': 'כן', 'col8': "I'm running this venture since 2018",
         'col9': 'From a competition perspective, providing a unique focus on VR social simulations for children diagnosed with ASD:\nFloreo - A VR learning tool designed for people on the ASD autistic spectrum. The Zoom app is designed for both adults and children and focuses on skills in general and not just social skills. https://floreotech.com.  The Autism Glass Project - A system developed at Stanford University, which includes the use of artificial intelligence and laminated reality using Google Glasses (Google Glass). The system focuses on one skill of identifying emotions and also addresses a specific population. Unlike our app, which focuses on a wide range of skills, including the children who have difficulty in the social field. The advantage of the Stanford system is that it allows for real-time response, not just a therapeutic tool. But it also has a different purpose from our app that deals with learning and coaching process, rather than a real-time support system.\nhttp://autismglass.stanford.edu ',
         'col10': 'As mention above, there is a need for therapeutic intervention for children with social difficulties. Solutions are accessible to 1:9 kids. The product uniqueness has two main aspects: first, an exclusive system that combines the benefits of the VR technology with an evidenced-based CBT social skills protocol – which no software has performed before. second, enable social skills training independently by the virtual instructor, as well as a tool for therapists'}

    ]

    return render(request, 'home.html', {'rows': rows})
