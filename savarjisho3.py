check = float(input("ჩეკის თანხა: "))
tip_percent = int(input("ჩაის ფული (%): "))
people = int(input("ადამიანების რაოდენობა: "))

tip = check * tip_percent / 100
total = check + tip
per_person = total / people

print("ჩაის ფული:", round(tip, 2))
print("სულ გადასახდელი:", round(total, 2))
print("თითო ადამიანზე:", round(per_person, 2))
