correct_password = "python2024"

for i in range(3):
    password = input("შეიყვანე პაროლი: ")
    left = 2 - i

    if password == "":
        print("შეავსეთ ველი. დარჩენილი მცდელობა:", left)
        continue

    if password == correct_password:
        print("წვდომა დაშვებულია")
        break

    print("არასწორი პაროლი. დარჩენილი მცდელობა:", left)
else:
    print("ანგარიში დაბლოკილია")
