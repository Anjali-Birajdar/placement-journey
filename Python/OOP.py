# object = bundle of similar attributes and methods

from car import Car


car1 = Car("Audi", 2025, "White", False)
car2 = Car("Rapid", 2017, "Beige", True)

print(car1.color)
print(car1.year)
print(car1.model)
print(car1.for_sale)

print(car2.color)
print(car2.year)
print(car2.model)
print(car2.for_sale)

car1.drive()
car2.stop()

car1.describe()
