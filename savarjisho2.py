seconds = int(input("შეიყვანე წამების რაოდენობა: "))

hours = seconds // 3600
left = seconds % 3600
minutes = left // 60
sec = left % 60

print(hours, "საათი", minutes, "წუთი", sec, "წამი")
