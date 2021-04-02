class MyFisrtClass:
    my_first_attribute = "1st Attrib"


class Car:
    def __init__(self, color, vmax, brand):
        self.color = color
        self.maxspeed = vmax
        self.car_brand = brand

    def present_yourself(self):
        print("I am a", self.color, self.car_brand, "my top speed is", self.maxspeed)