prices = {"ლეპტოპი": 2500, "მაუსი": 40, "კლავიატურა": 120, "მონიტორი": 650}
stock = {"ლეპტოპი": 2, "მაუსი": 10, "კლავიატურა": 1, "მონიტორი": 3}
orders = [
    ("ნინო", "ლეპტოპი", 1),
    ("გიორგი", "მაუსი", 3),
    ("ანა", "კლავიატურა", 1),
    ("ნინო", "მაუსი", 2),
    ("გიორგი", "კლავიატურა", 1),
    ("ანა", "ტელეფონი", 1),
    ("ლუკა", "ლეპტოპი", 1),
    ("ლუკა", "მონიტორი", 5),
]

spent = {}
failed = set()

for name, product, quantity in orders:
    if product not in prices:
        print(f"❌ {name}: '{product}' არ იყიდება")
        failed.add(name)
    elif stock[product] < quantity:
        print(f"⚠️ {name}: {product} — მარაგში მხოლოდ {stock[product]} ცალია")
        failed.add(name)
    else:
        stock[product] = stock[product] - quantity
        amount = prices[product] * quantity
        print(f"✅ {name}: {product} x{quantity} = {amount} ლარი")

        if name in spent:
            spent[name] = spent[name] + amount
        else:
            spent[name] = amount

print("--- ანგარიში ---")

total = 0
for name, amount in spent.items():
    print(f"{name}: {amount} ლარი")
    total = total + amount

print(f"შემოსავალი: {total} ლარი")

sold_out = []
for product, amount in stock.items():
    if amount == 0:
        sold_out.append(product)

print("ამოიწურა:", sorted(sold_out))
print("წარუმატებელი შეკვეთა ჰქონდათ:", sorted(failed))
