print("=== სტუდენტის შეფასების სისტემა ===")

try:
    name = input("სტუდენტის სახელი: ").strip()
    initial = name[0]
    score = int(input("მიღებული ქულა: "))
    max_score = int(input("მაქსიმალური ქულა: "))
    percent = score / max_score * 100
except IndexError:
    print("❌ სახელი ცარიელი ვერ იქნება")
except ValueError:
    print("❌ ქულები მთელი რიცხვებით ჩაწერეთ")
except ZeroDivisionError:
    print("❌ მაქსიმალური ქულა 0 ვერ იქნება")
else:
    if score < 0 or score > max_score:
        print("❌ ქულა არასწორ დიაპაზონშია")
    else:
        if percent >= 91:
            grade = "A"
        elif percent >= 81:
            grade = "B"
        elif percent >= 71:
            grade = "C"
        elif percent >= 61:
            grade = "D"
        elif percent >= 51:
            grade = "E"
        elif percent >= 41:
            grade = "FX"
        else:
            grade = "F"
        print(f"✅ {initial}. {name} — {percent}% — შეფასება: {grade}")
finally:
    print("შეფასების სისტემამ მუშაობა დაასრულა")
