age = int(input("ასაკი: "))
parent = input("მშობელთან ერთად ხართ? (კი/არა): ").strip()

if age >= 18 or (age >= 12 and parent == "კი"):
    print("შესვლა დაშვებულია")
else:
    print("შესვლა აკრძალულია")
