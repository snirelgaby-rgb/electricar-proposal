import os

# נתיב ה-GitHub שלך
base_path = r'C:\Users\SNIR\Desktop\הצעות מחיר - אלקטריקר\2026 הצעות מחיר - אלקטריקר'

def generate_interactive_quote():
    print("--- יצירת הצעת מחיר אינטראקטיבית ---")
    
    # איסוף נתונים
    name_he = input("שם לקוח (עברית): ")
    name_ru = input("שם לקוח (רוסית/אנגלית): ")
    price = input("מחיר סופי ללא מע\"מ (למשל 5900): ")
    folder_name = input("שם תיקייה לקישור (למשל yulia-nikolov): ")

    # קריאת התבנית
    try:
        with open('template.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ שגיאה: קובץ template.html לא נמצא בתיקייה!")
        return

    # הזרקת הנתונים - כאן הקסם קורה
    content = content.replace('{{CUSTOMER_NAME_HE}}', name_he)
    content = content.replace('{{CUSTOMER_NAME_RU}}', name_ru)
    content = content.replace('{{TOTAL_PRICE}}', price)

    # יצירת התיקייה
    target_path = os.path.join(base_path, folder_name)
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    # שמירה
    with open(os.path.join(target_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ בוצע! התיקייה '{folder_name}' מוכנה לסנכרון ב-GitHub Desktop.")

if __name__ == "__main__":
    generate_interactive_quote()