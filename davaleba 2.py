card = "4111222233334444"
phone = "599123456"

masked = "**** **** **** " + card[-4:]

print("შენიღბული:", masked)
print("პირველი 4 ციფრი:", card[:4])
print("ციფრების რაოდენობა:", len(card))
print("შებრუნებული:", card[::-1])
print("ტელეფონი:", phone[:3], phone[3:5], phone[5:7], phone[7:])
