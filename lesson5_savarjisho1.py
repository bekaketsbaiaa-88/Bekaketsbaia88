amount = float(input("ყიდვის თანხა (ლარი): "))
promo = input("პრომო-კოდი (თუ არ გაქვთ — Enter): ")

if amount >= 200:
    discount = 20
elif amount >= 100:
    discount = 10
elif amount >= 50:
    discount = 5
else:
    discount = 0

price = amount - amount * discount / 100

if promo.upper() == "VIP":
    price = price - 5
    print("🎁 VIP კოდი: დამატებით -5 ლარი")

print(f"ფასდაკლება: {discount}%")
print(f"გადასახდელი: {price:.2f} ლარი")
