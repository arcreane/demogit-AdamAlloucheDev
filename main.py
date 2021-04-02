from OOP.classes import *

my_first = MyFisrtClass()
my_second = MyFisrtClass()

print("Appel de my_attribute depuis ma classe : ", MyFisrtClass.my_first_attribute)
print("Appel de my_attribute dans ma premiere variable : ", my_first.my_first_attribute)
print("Appel de my_attribute dans ma deuxieme variable : ", my_second.my_first_attribute)

MyFisrtClass.my_first_attribute = "depuis ma classe"
my_first.my_first_attribute = "depuis ma 1ere variable"
my_second.my_first_attribute = "depuis ma 2eme variable"

print("Appel de my_attribute depuis ma classe : ", MyFisrtClass.my_first_attribute)
print("Appel de my_attribute dans ma premiere variable : ", my_first.my_first_attribute)
print("Appel de my_attribute dans ma deuxieme variable : ", my_second.my_first_attribute)

my_car = Car("Red", 300, "Ferrari")
my_other_car = Car("Green", 320, "Lamborghini")

my_car.present_yourself()
my_other_car.present_yourself()

f1 = my_car.present_yourself
f2 = my_other_car.present_yourself

f1()
f2()
