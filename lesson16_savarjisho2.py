class Car:
    wheels = 4

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year


car1 = Car("BMW", "შავი", 2020)
car2 = Car("Toyota", "თეთრი", 2018)

print(car1.brand, car1.wheels)
print(car2.brand, car2.wheels)

car2.wheels = 3

print(car1.wheels)
print(car2.wheels)
print(Car.wheels)

# car2.wheels = 3 კლასის ატრიბუტს არ ცვლის. ის car2-ს თავის საკუთარ wheels ატრიბუტს უქმნის.
# ამიტომ car2.wheels არის 3.
# car1-ს საკუთარი wheels არ აქვს, ამიტომ კლასის მნიშვნელობას იღებს, ანუ 4-ს.
# Car.wheels კლასის ატრიბუტია და ის არავის შეუცვლია, ამიტომ ისევ 4-ია.
