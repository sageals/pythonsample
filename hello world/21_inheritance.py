class Mamels:
    def walk(self):
        print("Walk")


class Dog(Mamels):
    pass


class Cat(Mamels):
    pass


dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.walk()

