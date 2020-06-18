from Animal import Animal


class Dog(Animal):

    def call_out(self):
        print("{}在叫唤".format(self.breed))


class Cat(Animal):

    def call_out(self):
        print("{}在叫唤".format(self.breed))

    def eat(self):
        print("{}在吃饭".format(self.name))


cat = Cat()
cat.eat()
cat.call_out()
