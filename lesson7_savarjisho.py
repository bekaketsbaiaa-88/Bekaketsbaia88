orders = ["ყავა", "ჩაი", "ყავა", "წვენი", "ჩაი", "ყავა", "წყალი"]

# ა) უნიკალური პროდუქტები
unique = []
for product in orders:
    if product not in unique:
        unique.append(product)

print("უნიკალური:", unique)

# ბ) სიხშირის ლისტი
frequency = [(product, orders.count(product)) for product in unique]

print("სიხშირე:", frequency)

# გ) ყველაზე პოპულარული
popular = ""
popular_count = 0
for product, amount in frequency:
    if amount > popular_count:
        popular = product
        popular_count = amount

print(f"ყველაზე პოპულარული: {popular} ({popular_count}-ჯერ)")

# დ) ბოლო 3 შეკვეთა
last_three = orders[-1:-4:-1]

print("ბოლო 3 შეკვეთა:", last_three)
