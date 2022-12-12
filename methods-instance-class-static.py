class car:
    obj_num = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

        car.obj_num += 1

    # using instance method !
    def show(self):
        print(f"the car name is {self.name} and the price is {self.price} ! and {car.obj_num} car/s is created !")

    # using class method !
    @classmethod
    def burden(cls, name, price):
        return cls(name, price)

    # static method !
    @staticmethod
    def expensive(price):
        if (price > 200):
            print(f" {price} $ is expensive ! ")
        else:
            print(f"{price} $ is suitable !")


car1 = car("BMW", 100)
car1.show()
car2 = car("Benz", 888)
car2.show()
# using class method
car3 = car.burden("Audi", 555)
car3.show()
# using static method
car.expensive(300)
