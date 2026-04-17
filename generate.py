import os
import json

def generate_interactive_quote():
    print("\n" + "="*30)
    print("--- יצירת הצעה חדשה - אלקטריקר ---")
    print("="*30 + "\n")
    
    name_he = input("שם לקוח (עברית): ")
    name_ru = input("שם לקוח (רוסית): ")
    name_en = input("שם לקוח (אנגלית): ")
    address = input("כתובת הלקוח: ")
    price = input("מחיר סופי: ")
    folder_name = input("שם תיקייה (באנגלית): ")

    labels = [
        "1. פריסת כבל ואורכו",
        "2. סוג חיבור (לוח פרטי, מונה, ציבורי)",
        "3. אספקת עמדה",
        "4. התקנת פאקט/ממסר פחת",
        "5. התקנת עמוד לעמדה",
        "6. הארקה מקומית",
        "7. משתלבות/אספלט",
        "8. ארון לעמדה",
        "9. תוספות",
        "10. תוספות"
    ]

    scope_data = {"he": [], "ru": [], "en": []}
    
    print("\n" + "-"*30)
    print("מילוי סעיפי ההצעה (Enter לדילוג)")
    print("-"*30)

    for i in range(10):
        print(f"\n>>> {labels[i]}")
        title_he = input(f"כותרת (עברית): ")
        
        if title_he:
            body_he = input(f"פירוט (עברית): ")
            title_ru = input(f"כותרת (רוסית): ") or ""
            body_ru = input(f"פירוט (רוסית): ") if title_ru else ""
            title_en = input(f"כותרת (אנגלית): ") or ""
            body_en = input(f"פירוט (אנגלית): ") if title_en else ""
            
            scope_data["he"].append({"title": title_he, "body": body_he})
            scope_data["ru"].append({"title": title_ru, "body": body_ru})
            scope_data["en"].append({"title": title_en, "body": body_en})
        else:
            scope_data["he"].append({"title": "", "body": ""})
            scope_data["ru"].append({"title": "", "body": ""})
            scope_data["en"].append({"title": "", "body": ""})

    try:
        with open('template.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace('{{CUSTOMER_NAME_HE}}', name_he)
        content = content.replace('{{CUSTOMER_NAME_RU}}', name_ru)
        content = content.replace('{{CUSTOMER_NAME_EN}}', name_en)
        content = content.replace('{{CUSTOMER_ADDRESS}}', address)
        content = content.replace('{{TOTAL_PRICE}}', price)
        content = content.replace('{{SCOPE_ITEMS_JSON}}', json.dumps(scope_data, ensure_ascii=False))

        target_path = os.path.join(os.getcwd(), folder_name)
        if not os.path.exists(target_path): os.makedirs(target_path)
        
        with open(os.path.join(target_path, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✅ הצלחה! התיקייה '{folder_name}' נוצרה.")
    except Exception as e:
        print(f"\n❌ שגיאה: {e}")

if __name__ == "__main__":
    generate_interactive_quote()