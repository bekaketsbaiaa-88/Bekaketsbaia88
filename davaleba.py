raw_username = " Super_Coder_2026 "

username = raw_username.strip().lower().replace("_", "-")

print("მომხმარებლის სახელი:", username)
print("სიგრძე:", len(username))
print("იწყება 'super'-ით:", username.startswith("super"))
print("ტირეების რაოდენობა:", username.count("-"))
print("მხოლოდ ასოები და ციფრები:", username.replace("-", "").isalnum())
