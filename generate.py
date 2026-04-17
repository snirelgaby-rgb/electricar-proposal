import os

def generate_interactive_quote():
    print("--- יצירת הצעה חדשה - אלקטריקר ---")
    
    # איסוף נתונים מהמשתמש
    name_he = input("הכנס שם לקוח (עברית): ")
    name_ru = input("הכנס שם לקוח (רוסית): ")
    name_en = input("הכנס שם לקוח (אנגלית): ")
    address = input("הכנס כתובת לקוח: ")
    price = input("הכנס מחיר סופי (מספר בלבד): ")
    folder_name = input("שם תיקייה לקישור (באנגלית, ללא רווחים): ")

    # קריאת תבנית ה-HTML
    try:
        with open('template.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ שגיאה: קובץ template.html לא נמצא בתיקייה!")
        return

    # הזרקת הנתונים לתוך ה-HTML
    content = content.replace('{{CUSTOMER_NAME_HE}}', name_he)
    content = content.replace('{{CUSTOMER_NAME_RU}}', name_ru)
    content = content.replace('{{CUSTOMER_NAME_EN}}', name_en)
    content = content.replace('{{CUSTOMER_ADDRESS}}', address)
    
    # פורמט למחיר (הוספת פסיקים לאלפים)
    try:
        formatted_price = f"{int(price):,}"
        content = content.replace('{{TOTAL_PRICE}}', formatted_price)
    except ValueError:
        content = content.replace('{{TOTAL_PRICE}}', price)

    # יצירת תיקיית היעד
    # וודא שהנתיב כאן הוא הנתיב שמעודכן אצלך ב-GitHub Desktop
    base_path = os.getcwd() 
    target_path = os.path.join(base_path, folder_name)
    
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    # שמירת הקובץ החדש
    with open(os.path.join(target_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ בוצע! התיקייה '{folder_name}' מוכנה.")
    print(f"עבור ל-GitHub Desktop כדי לבצע Commit ו-Push.")

if __name__ == "__main__":
    generate_interactive_quote()