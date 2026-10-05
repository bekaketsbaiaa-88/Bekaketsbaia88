word = input("შეიყვანე სიტყვა: ")
symbol = input("რომელი სიმბოლო დავთვალოთ: ")

count = 0
for letter in word:
    if letter == symbol:
        count = count + 1

print("სიმბოლო", symbol, "გვხვდება", count, "-ჯერ")
