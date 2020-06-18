class Person:

    def __init__(self):
        self.__age = 20

        # @property
        # def age(self):
        #     return self.__age
        #
        # @age.setter
        # def age(self, value):
        #     self.__age = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    age = property(get_age, set_age)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


person = Person()
print("person=%s" % id(person))

person1 = Person()
print(id(person1))

person2 = Person()
print(id(person2))
