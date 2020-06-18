class Animal:
    __name = ""

    def __init__(self, breed="小猫", name="团团"):
        self.breed = breed
        self.name = name

    def eat(self):
        print("{}{}在吃饭".format(self.breed, self.name))
