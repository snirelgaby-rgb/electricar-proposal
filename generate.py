import os

# --- 1. הגדרות נתיב ---
base_path = r'C:\Users\SNIR\Desktop\2026 רישום תובלה - ראקטיקה\הצעות מחיר - אלקטריקה\electricar proposal' 

print("--- מחולל הצעות מחיר אלקטריקה - גרסה מעוצבת מלאה ---")

# --- 2. איסוף נתונים ---
customer_name = input("הכנס שם לקוח מלא: ")
total_price = input("הכנס מחיר סופי (לדוגמה 5,900): ")
folder_id = input("שם תיקייה באנגלית (לדוגמה: yulia-nikolov): ")

customer_folder = os.path.join(base_path, folder_id)
if not os.path.exists(customer_folder):
    os.makedirs(customer_folder)

file_path = os.path.join(customer_folder, "index.html")

# --- 3. ה-HTML המלא (העתקתי את העיצוב שלך עם תיקון סוגריים) ---
html_content = f"""
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>הצעת מחיר | {customer_name}</title>
    <style>
        /* כאן הכפלתי את הסוגריים כדי שלא תהיה שגיאה */
        body {{ font-family: 'Segoe UI', sans-serif; background-color: #f4f7f9; margin: 0; padding: 20px; direction: rtl; }}
        .container {{ max-width: 800px; margin: auto; background: white; padding: 40px; border-radius: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.1); border-top: 8px solid #1a3a5f; }}
        .header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #eee; padding-bottom: 20px; }}
        .logo {{ color: #1a3a5f; font-size: 24px; font-weight: bold; }}
        .quote-title {{ color: #c9a84c; font-size: 32px; margin: 20px 0; }}
        .details-table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        .details-table th, .details-table td {{ padding: 12px; border: 1px solid #eee; text-align: right; }}
        .details-table th {{ background: #f9f9f9; color: #555; }}
        .total-section {{ background: #1a3a5f; color: white; padding: 20px; border-radius: 10px; text-align: center; margin-top: 30px; }}
        .total-price {{ font-size: 38px; font-weight: bold; color: #c9a84c; }}
        .footer {{ margin-top: 40px; text-align: center; color: #888; font-size: 14px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">ELECTRI-CAR</div>
            <div>תאריך: 14/04/2026</div>
        </div>
        
        <h1 class="quote-title">הצעת מחיר עבור {customer_name}</h1>
        
        <p>להלן פירוט העבודה עבור התקנת עמדת טעינה לרכב חשמלי:</p>
        
        <table class="details-table">
            <thead>
                <tr>
                    <th>תיאור השירות</th>
                    <th>כמות</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>התקנת עמדת טעינה כולל פריסת תשתית</td>
                    <td>1</td>
                </tr>
                <tr>
                    <td>אביזרי קצה והגנות חשמליות</td>
                    <td>1</td>
                </tr>
            </tbody>
        </table>

        <div class="total-section">
            <div>סה"כ לתשלום (לא כולל מע"מ):</div>
            <div class="total-price">{total_price} ₪</div>
        </div>

        <div class="footer">
            <p>הצעה זו תקפה ל-30 יום | אלקטריקה - פתרונות טעינה מתקדמים</p>
        </div>
    </div>
</body>
</html>
"""

# --- 4. שמירה ---
try:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"\n✅ הצלחה! נוצרה הצעה מושלמת עבור {customer_name}")
    print(f"📍 הקובץ מחכה לך ב-GitHub Desktop")
except Exception as e:
    print(f"❌ שגיאה: {e}")