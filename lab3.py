def my_decorator(func):
    def wrapper(self,vel,hei):
        print("Price in dollars: ")
        print(func(self, self.maxVelocity, self.maxHeight))
        print("Price in hruvnyas: ")
        print(func(self, self.maxVelocity, self.maxHeight)*28)
        return func(self, self.maxVelocity, self.maxHeight)
    return wrapper


class Plane:
    colour = "white"

    def __init__(self, brand="brand", model="model", maxVelocity=100, maxHeight=1000):
        self.brand = brand
        self._model = model
        self.__maxVelocity = maxVelocity
        self.__maxHeight = maxHeight

    def __str__(self):
        return f"Parameters: {self.brand}, {self._model}, {self.__maxHeight}, {self.__maxVelocity}"
    
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def maxVelocity(self):
        if self.__maxVelocity < 100:
            self.__maxVelocity = 100
        return self.__maxVelocity

    @maxVelocity.setter
    def maxVelocity(self, maxVelocity):
        self.__maxVelocity = maxVelocity

    @property
    def maxHeight(self):
        if self.__maxHeight < 1000:
            self.__maxHeight = 1000
        return self.__maxHeight

    @maxHeight.setter
    def maxHeight(self, maxHeight):
        self.__maxHeight = maxHeight

    @staticmethod
    def price(maxV, maxH):
        return maxV * 1000 + maxH * 100

    def colour_disp(self):
        print(self.colour)


class Fighter(Plane):
    colour = "green"

    def __init__(self, brand, model, maxVelocity, maxHeight):
        super().__init__(brand, model, maxVelocity, maxHeight)

    @staticmethod
    def kmph_to_mph(maxVelocity):
        return maxVelocity * 1000

    @my_decorator
    def price(self, maxVelocity, maxHeight):
        return (self.kmph_to_mph(maxVelocity) + maxHeight * 100) * 2


d_plane = Plane()
print(d_plane)

my_plane = Plane("Airbus", "Boeing", 300, 2000)
print(my_plane)
print("Price: ", my_plane.price(my_plane.maxVelocity, my_plane.maxHeight))

my_fighter = Fighter("Hawk", "Fighter", 800, 1000)
print(my_fighter)
print("Price: ", my_fighter.price(my_fighter.maxVelocity, my_fighter.maxHeight))
my_fighter.colour = "brown"
print(my_fighter.colour)
Plane.colour_disp(my_plane)

my_fighter.maxHeight=100
print(my_fighter.maxHeight)

print(Fighter.colour)
