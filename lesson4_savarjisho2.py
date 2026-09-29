a = int(input("პირველი რიცხვი: "))
b = int(input("მეორე რიცხვი: "))
c = int(input("მესამე რიცხვი: "))

if a >= b and a >= c:
    biggest = a
elif b >= a and b >= c:
    biggest = b
else:
    biggest = c

print("უდიდესი რიცხვია:", biggest)
