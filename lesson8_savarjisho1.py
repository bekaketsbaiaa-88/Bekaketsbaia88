text = "Python არის მარტივი, Python არის ძლიერი და Python პოპულარულია."

clean_text = text.lower().replace(",", "").replace(".", "")
words = clean_text.split()

counts = {}
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

for word, amount in counts.items():
    print(f"{word}: {amount}")

top_word = ""
top_count = 0
for word, amount in counts.items():
    if amount > top_count:
        top_word = word
        top_count = amount

print(f"ყველაზე ხშირი: '{top_word}' ({top_count}-ჯერ)")
print("სხვადასხვა სიტყვა:", len(counts))
